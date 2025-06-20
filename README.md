This works: `uvx --from git+ssh://git@github.com/asmith26/debug-uvx-gitlfs.git@no-gitlfs my_package`

These don't work:
- `uvx --from git+ssh://git@github.com/asmith26/debug-uvx-gitlfs.git my_package`
- `uvx --from git+ssh://git@github.com/asmith26/debug-uvx-gitlfs.git my_package_gitlfs`
