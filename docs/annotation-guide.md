# Rip current annotation guide

This guide defines how to label the rip-current dataset in a consistent, reviewable way.

## Label classes

Use three labels only:

- `positive`: the image contains a visually supported rip-current channel or plume.
- `negative`: the image does not contain a supported rip current.
- `review`: the image is ambiguous or too uncertain for a reliable label.

Only train on `positive` and `negative` records. Keep `review` examples aside and audit them before use.

## What counts as a positive rip-current sign

A positive label should be supported by at least one of the following visible cues:

- a narrow channel of darker, foamier, or calmer water moving away from shore;
- a gap or break in the surf line where waves are not breaking across the same width;
- foam, sand, or debris moving offshore in a narrow plume;
- a channel cut through the sandbar or nearshore region;
- water discoloration or visible current direction away from the beach.

A box should cover the visible rip-current region, not the entire beach or full surf zone.

## What counts as a negative example

Negative images can still contain surf, turbulence, sand, foam, or wave gaps, but they should not show a convincing offshore flow channel. Examples include:

- normal beach surf without a visible channel;
- wave shadows and lighting effects;
- harmless backwash or sediment movement;
- deep water or open ocean without a clear current signature;
- shoreline geometry that looks unusual but does not have an offshore channel.

## What counts as a review example

Use `review` for images where:

- the rip current is partially blocked by glare, spray, or poor resolution;
- the scene is too dark, too distant, or too zoomed out to decide;
- several possible explanations exist and a second reviewer is needed.

Do not force uncertain images into the training set.

## Bounding box rules

When annotating a positive image:

1. draw one tight box around the strongest visible rip-current feature;
2. include the channel, plume, or offshore-labeled water region only;
3. avoid boxing the full shoreline or broad sections of the beach;
4. use a square-ish or rectangular box that follows the current shape.

The YOLO label format is:

```text
0 center_x center_y width height
```

Coordinates are normalized to `[0, 1]`.

## Common lookalikes to watch for

The model should learn to distinguish rip currents from:

- ordinary wave gaps;
- shadows and bright glare;
- backwash flowing down the beach;
- sediment plumes that are not clearly directed offshore;
- deep water or darker ocean patches without a channel shape;
- sandbars and shore geometry that resemble a current but are not one.

## Review process

- One person labels a batch.
- A second reviewer checks a sample of positive and difficult images.
- Record disagreements and update the annotation guide.
- Keep the dataset provenance and unblurred source metadata in the manifest.

This is a safety-focused research project. The goal is to study visual risk cues, not to replace lifeguards or official beach warnings.
