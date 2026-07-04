---
name: ue5-angelscript
description: Use for Unreal Engine projects using Hazelight-style AngelScript gameplay code, especially translating C++ Unreal patterns into `.as` scripts, checking script binding differences, adding narrow project C++ fallbacks, and validating Blueprint-exposed script behavior.
---

# UE5 AngelScript

Use AngelScript as the gameplay layer when the project is built on the
UnrealEngine-Angelscript fork. Translate the Unreal pattern, not the exact C++
syntax.

## Workflow

1. Read project-local guidance and existing `.as` examples.
2. Search the current scripts for the same gameplay pattern before inventing a
   new binding shape.
3. Check the actual script API when a C++ macro, override, or helper does not
   compile.
4. Add project C++ only for a narrow binding gap that script cannot express.
5. Validate with script reload and live PIE when behavior is player-visible.

## Rules

- Keep one class per `.as` file unless the project convention says otherwise.
- Use script annotations such as `UCLASS`, `UPROPERTY`, and `UFUNCTION`, not C++
  generated-body macros.
- Do not assume C++ functions, macros, or override names are script-visible.
- Use project examples for components, delegates, timers, spawn helpers,
  replication, Enhanced Input, and Blueprint property exposure.
- For Blueprint-driven script defaults, read back both the Blueprint CDO and any
  placed map instances that matter.

## Hard Lessons

- Binding names can differ from C++; verify before copying course or sample
  code.
- A gameplay action helper should usually own shared assertions and spawn
  behavior rather than duplicating checks per input action.
- Controller rotation is often the correct source for player aiming even when
  actor rotation appears plausible.
- Direct function calls prove script wiring only. They do not prove player input
  routing or possession.
