# GitHub Copilot Workspace Setup

This directory contains reusable Copilot customization.

## Agents
- Ask: read-only technical Q&A.
- Plan: read-only repository analysis and implementation planning.
- Reviewer: read-only senior code review.
- Debugger: read-only root-cause investigation.

## Instructions
Instructions are automatically applied according to their `applyTo` patterns.

## Skills
Skills provide reusable workflows for common engineering tasks.

## Recommended workflow

Ask -> understand the problem
Plan -> inspect and design the solution
Agent -> implement
Reviewer -> review the implementation
Debugger -> investigate failures

## Notes

Keep these files under version control so the Copilot behavior is reusable across machines and team members.
