---
name: ue5-perforce
description: Use for UE5 Perforce workspaces, especially checkout-before-write, named changelists, binary asset coordination, default changelist isolation, map/content submit hygiene, overlapping clients, and submitted readbacks.
---

# UE5 Perforce

UE projects contain merge-hostile binary assets. Treat source control as part of
the implementation workflow, not a final afterthought.

## Rules

- Open files before editing.
- Use a named changelist for each coherent task.
- Never submit the default changelist.
- Never sweep the default changelist into a task CL.
- Check binary locks before editing `.uasset` or `.umap` files.
- Protect engine/imported paths unless the user explicitly owns that work.
- After editor asset moves, immediately inspect the default CL and reopen only
  the intended depot paths into the task CL.

## Before Submit

Read back:

```text
p4 describe -s <CL>
p4 opened -c <CL>
p4 opened -c default
```

Resolve unrelated default-CL files by leaving them untouched unless the user
explicitly asks. After submit, use:

```text
p4 describe -s <submittedCL>
p4 fstat -T headRev,headChange <representative files>
```

An empty `p4 opened -c <CL>` after submit usually means the CL closed. It is not
proof by itself; use `describe` and `fstat`.

## Overlapping Clients

Large UE workspaces may have overlapping engine and project clients. Choose cwd
deliberately so the nearest `.p4config` owns the files being changed. If a task
crosses clients, split into companion CLs and report that boundary.
