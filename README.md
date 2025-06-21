To get it to work, following https://github.com/astral-sh/uv/issues/14173#issuecomment-2993547003

```bash
$ rm -rf $(uv cache dir)/git-v0
$ export UV_GIT_LFS=1 && uvx --from git+ssh://git@github.com/asmith26/debug-uvx-gitlfs.git my_package_gitlfs

# Works, prints "Hello my_package_gitlfs!"
```


---

This works: `uvx --from git+ssh://git@github.com/asmith26/debug-uvx-gitlfs.git@no-gitlfs my_package`

These don't work:
- `uvx --from git+ssh://git@github.com/asmith26/debug-uvx-gitlfs.git my_package`
- `uvx --from git+ssh://git@github.com/asmith26/debug-uvx-gitlfs.git my_package_gitlfs`
