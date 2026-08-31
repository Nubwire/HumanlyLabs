# 1. Record architecture decisions

Date: 2026-08-31

## Status

Accepted

## Context

Humanly Labs has been developed iteratively (this repo picks up at "v41" of
the site export) without a written record of why particular technical
choices were made. Work on this project happens across disconnected sessions
with no shared memory, so decisions and their reasoning need to live
somewhere durable and discoverable, not in chat history.

## Decision

We will use Architecture Decision Records, as described by Michael Nygard,
to record any decision with lasting architectural or operational impact
(hosting, data flow, third-party integrations, security posture, etc.).

## Consequences

Anyone — human or AI assistant — picking up this project can read `adr/` to
understand not just what the current setup is, but why, without having to
reconstruct reasoning from the code or ask around.
