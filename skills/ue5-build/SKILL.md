---
name: ue5-build
description: Use for UE5 build, rebuild, generated project files, UnrealBuildTool, UnrealHeaderTool, commandlet, packaging, cook, ShaderCompileWorker, and missing-module validation workflows.
---

# UE5 Build

Use builds deliberately. Full UE builds are expensive, but they are required
when reflected C++, modules, plugins, packaging, or runtime cook behavior is in
scope.

## Build When

- C++ source, `.Build.cs`, `.Target.cs`, `.uproject`, or plugin config changes.
- New or changed `UCLASS`, `USTRUCT`, `UENUM`, `UFUNCTION`, or `UPROPERTY`
  declarations need UHT.
- The editor reports missing modules or modules built for another engine
  version.
- Packaging, cook rules, Primary Assets, soft references, or runtime startup
  behavior are part of the task.

## Usually Skip Full Build When

- Only script files changed and the project supports live script reload.
- Only data assets changed and editor readback plus PIE is enough.
- Only docs, tasks, or validation notes changed.

## Commands To Locate

Project-specific docs should define exact paths for:

- `GenerateProjectFiles.bat`;
- `Engine/Build/BatchFiles/Build.bat <EditorTarget> Win64 Development`;
- `ShaderCompileWorker` build;
- UAT `BuildCookRun`;
- commandlet Blueprint compile or asset validation.

## Validation

- Keep the build command and success/failure summary.
- Fix the first real UBT/UHT/UAT error, then rerun.
- For packaged changes, inspect staged manifests and run a packaged smoke when
  practical.
- Pair build success with PIE or runtime validation for gameplay-visible work.
