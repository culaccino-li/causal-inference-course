# GitHub 发布指南 / GitHub Publishing Guide

## 一、中文（首次上传）

1. 在 GitHub 点击 **New repository**，仓库名建议设为 `causal-inference-course`，简介可填写：`政治与社会科学因果推断交互式课程｜Interactive Causal Inference Course`。如希望使用GitHub Pages的免费公开发布，建议选 **Public**。
2. **不要直接上传 ZIP 文件作为网站。** 先在电脑上解压发布包，进入解压后的文件夹，确认里面直接有 `index.html`、`lessons/`、`README.md`、`version.json` 等文件。
3. 打开刚创建的仓库，选择 **Add file → Upload files**（空仓库可选 **uploading an existing file**）；把解压后文件夹内的**所有文件和 `lessons/` 文件夹**拖入上传区域，提交到 `main`。不要把整个项目包当作一个单独ZIP文件上传。
4. 打开仓库 **Settings → Pages → Build and deployment → Source: Deploy from a branch**；选择 **Branch: main**，目录 **/(root)**，保存。等待 GitHub 完成构建。
5. 网站预计位于 `https://culaccino-li.github.io/causal-inference-course/`。这只是按推荐仓库名推算的地址，仓库、发布设置实际生效前不能视为已上线。
6. 开启后检查首页、任意讲次、跳页、全屏与返回首页；由于浏览器安全策略，原生全屏可能需要用户点击并授权，页面应提供窗口演示模式。

## 二、中文（版本管理）

- 代码文件保持稳定：`index.html`、`lessons/lesson_06.html` 等。
- 使用 `v2.0.1`、`v2.0.2`、`v2.1.0` 作为 **Git tag / Release** 名称；时间在 Release 标题与 `CHANGELOG.md` 中记录（如 `2026-10-24`）。
- **补丁版本**：修复导航或文字错误，例如 `v2.0.2`。
- **次版本**：增强Conjoint交互或新增一个独立功能，例如 `v2.1.0`。
- **主版本**：重大课程架构或兼容性调整，例如 `v3.0.0`。
- 第一次发布后，在仓库点击 **Releases → Draft a new release**，建立标签 `v2.0.1`，标题为 `v2.0.1 — 2026-10-24 | 14-module interactive course`，可将发布 ZIP 作为附件。
- 每次更新先修改代码、`version.json`、`VERSION` 与 `CHANGELOG.md`，提交 commit 后再创建新Release；尽量避免重写已经发布的版本标签。

## Three: English (first publication)

1. Create a public repository named **`causal-inference-course`** (or another stable repository name).
2. **Extract the ZIP first**. The repository root must directly contain `index.html`, the `lessons/` directory, and `README.md`. Uploading the ZIP alone does not create a functioning website.
3. In the new repository, select **Add file → Upload files**, drag in the extracted contents (including the `lessons/` folder), and commit to `main`.
4. Open **Settings → Pages**. Under **Build and deployment**, select **Deploy from a branch**, then choose **main** and **/(root)**. Save.
5. After GitHub Pages publishes, check the expected URL `https://culaccino-li.github.io/causal-inference-course/`, adjusting the username/repository if needed.
6. Verify navigation to several lessons, in-lesson interactions, and fullscreen/return-home behavior.

## Four: English (versioned updates)

- Keep the repository and live website URL **stable**.
- Tag releases using `vMAJOR.MINOR.PATCH`, with ISO dates in `CHANGELOG.md` and `version.json`.
- Example release: `v2.0.1 — 2026-10-24`.
- Use GitHub **Releases → Draft a new release** to create the tag, add release notes, and optionally attach a ZIP package.
- PATCH = bug fix; MINOR = compatible improvement; MAJOR = major structural or compatibility change.

### Git (optional / 可选命令行方式)

```bash
git init
git add .
git commit -m "release: v2.0.1 (2026-10-24)"
git branch -M main
git remote add origin https://github.com/culaccino-li/causal-inference-course.git
git push -u origin main
git tag v2.0.1
git push origin v2.0.1
```

Run the commands from the **extracted project root**, after creating the empty GitHub repository. The remote URL assumes the suggested repository name and connected account. Git authentication is required.

### 安全与版权 / Safety and rights

GitHub Pages公开发布的网站可能被任何人访问，请确认课程内容、个人信息和外部素材适合公开；发布前不要上传密码、访问令牌或包含隐私数据的真实研究数据。仓库目前没有开放许可证，请在决定授权方式之后再添加合适的许可证。

---

Official references / 官方文档：
- https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site
- https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository
- https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository
