#!/usr/bin/env node

import { readFile } from "node:fs/promises";

const requiredSections = [
  "Objective",
  "Source-of-truth inputs",
  "Locked decisions",
  "Visual concept",
  "Typography",
  "Colour tokens",
  "Layout system",
  "Section map",
  "Imagery and iconography",
  "Components and interactions",
  "Motion system",
  "Responsive transformations",
  "Accessibility",
  "Factual integrity",
  "Approval status",
];

const briefPath = process.argv[2];

if (!briefPath) {
  console.error("Usage: node validate_design_brief.mjs <DESIGN-BRIEF.md>");
  process.exit(2);
}

let source;
try {
  source = await readFile(briefPath, "utf8");
} catch (error) {
  console.error(`Could not read ${briefPath}: ${error.message}`);
  process.exit(2);
}

const headingMatches = [...source.matchAll(/^#{1,6}\s+(.+?)\s*$/gm)];
const headings = new Set(headingMatches.map((match) => match[1].trim()));
const missingSections = requiredSections.filter((section) => !headings.has(section));
const unresolvedCount = (source.match(/\[TO BE CONFIRMED\]/g) || []).length;
const emptySections = [];

for (const section of requiredSections) {
  const headingIndex = headingMatches.findIndex(
    (match) => match[1].trim() === section,
  );
  if (headingIndex === -1) continue;

  const match = headingMatches[headingIndex];
  const contentStart = match.index + match[0].length;
  const nextMatch = headingMatches[headingIndex + 1];
  const contentEnd = nextMatch ? nextMatch.index : source.length;
  if (!source.slice(contentStart, contentEnd).trim()) emptySections.push(section);
}

const result = {
  valid: missingSections.length === 0 && emptySections.length === 0,
  path: briefPath,
  missingSections,
  emptySections,
  unresolvedCount,
};

console.log(JSON.stringify(result, null, 2));
process.exit(result.valid ? 0 : 1);
