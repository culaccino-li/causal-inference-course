# 政治与社会科学因果推断 · 交互式课程
# Interactive Causal Inference for Political and Social Science

**版本 / Version:** `v2.0.1` · **发布日期 / Release date:** `2026-10-24`  
**课程规模 / Scope:** 12讲主课 + 2讲实验专题 / 12 core lessons + 2 experimental-methods modules  
**内容语言 / Course language:** 中文 / Chinese  
**项目介绍 / Documentation:** 中文 / English

![课程首页 / Course homepage](assets/home-preview.png)

## 中文介绍

本项目是一套面向政治学与社会科学研究者的**可离线运行、可交互、逐页播放的因果推断课程**。课程包括12讲主课与2讲实验方法专题，共14个教学模块、约695个播放画面。内容涵盖因果推断基础、DAG、随机与调查实验、回归、匹配、固定效应、DID、RDD、IV、SCM、现代面板因果推断、因果机器学习以及研究设计与复现。

教学设计将公式和识别假设与可操作的数值模拟、DAG图、真实期刊论文精读、Stata/R示例及即时反馈练习结合。**教学模拟数据不代表论文原始数据。**

### 在线使用 / GitHub Pages

部署后的网站地址示例：**https://culaccino-li.github.io/causal-inference-course/**  
*注意：这是预期地址，只有创建仓库并启用 GitHub Pages 后才会生效。仓库名或账号不同，URL也不同。*

打开 [`index.html`](index.html) 进入课程主页；单独课程文件存放于 [`lessons/`](lessons/)。也可以直接下载整个项目，在本地以Chrome或Edge打开 `index.html`。

### 课程目录

| 编号 | 课程 |
| --- | --- |
| 01 | 因果推断导论 |
| 02 | DAG 与因果结构 |
| 02.5A | 随机实验与田野实验 |
| 02.5B | 调查实验与 Conjoint |
| 03 | 回归与因果识别 |
| 04 | 匹配与倾向得分 |
| 05 | 面板数据与固定效应 |
| 06 | 双重差分 DID |
| 07 | 断点回归 RDD |
| 08 | 工具变量 IV |
| 09 | 合成控制 SCM |
| 10 | 现代面板因果推断 |
| 11 | 因果机器学习 |
| 12 | 研究设计与复现 |

### 版本管理

- **仓库名固定**：`causal-inference-course`；不要在每次更新时重命名仓库。
- **Git标签 / Release**：`vMAJOR.MINOR.PATCH`，例如 `v2.0.1`。
- **发布日期**：`YYYY-MM-DD`，记录于 [`version.json`](version.json) 和 [`CHANGELOG.md`](CHANGELOG.md)。
- **建议规则**：`PATCH`修复链接、排版与错误；`MINOR`增加功能或扩充单讲；`MAJOR`重构课程架构或不兼容的导航。
- 历史版本通过 Git tags / Releases 保留，不在仓库根目录堆放 `index_old.html` 等备份文件。

详见 [`DEPLOYMENT_GUIDE.md`](DEPLOYMENT_GUIDE.md) 和 [`CHANGELOG.md`](CHANGELOG.md)。

## English Introduction

This repository hosts an **interactive, presentation-oriented course in causal inference for political and social science research**. It contains 12 core lessons and 2 experimental-methods modules (14 modules in total, with approximately 695 presentation screens).

Topics include potential outcomes, causal DAGs, randomized and survey experiments, regression and identification, matching, fixed effects, difference-in-differences, regression discontinuity, instrumental variables, synthetic control, modern panel-data methods, causal machine learning, and reproducible research design.

The course combines staged visual explanations with **interactive simulations, research-paper case studies, Stata/R examples, and formative quizzes**. Simulated teaching data are distinct from the original data and estimates reported in cited studies.

**Course language:** Chinese. **Repository documentation:** Chinese and English. The English description does not imply that all lesson pages have been translated.

### Run the site

- **Online:** Enable GitHub Pages from `main` / `(root)`. The expected URL, assuming the suggested account and repository name, is `https://culaccino-li.github.io/causal-inference-course/`.
- **Offline:** Download/extract the repository and open `index.html` in Chrome or Edge.
- **Project structure:** `index.html` is the stable entry point; lesson content is under `lessons/`.

### Versioning

Use stable file paths and a semantic tag such as `v2.0.1`, with a separate ISO release date (`2026-10-24`). Preserve earlier versions via Git tags and GitHub Releases rather than changing the live site's URL.

See [`DEPLOYMENT_GUIDE.md`](DEPLOYMENT_GUIDE.md) for bilingual step-by-step instructions.

## 学术与使用说明 / Academic and usage notes

本项目用于方法教学。引用的学术论文归其相应著作权人所有；外部论文链接不等于附带论文内容的再授权。仓库目前**未添加开源许可证**，公开可访问不表示任何人自动获得复制、修改或再发布课程材料的许可。发布前请确认你有权公开课程代码和内容，尤其是外部素材。

This repository is intended for teaching. Referenced papers remain subject to their respective rights holders. **No open-source license has been selected**; public visibility alone does not grant reuse rights. Confirm permissions for any third-party material before publishing.
