# Optimization-Homework-Simulations

This repository contains study materials for the course "Optimization Methods and Applications" (《最优化计算方法》). It includes personal learning notes, solutions to homework exercises, and practical simulation examples, along with their corresponding code (Python, MATLAB) and output files (images, .fig files).

## About This Repository

This project is a personal learning space dedicated to understanding and applying optimization techniques. The materials are organized chapter by chapter, following the structure of the course.

The main contents include:
* **Learning Notes:** HTML-based notes summarizing key concepts for each chapter.
* **Homework Exercises:** Detailed solutions and explanations for course exercises, often accompanied by Python or MATLAB code and visual outputs.
* **Simulation Examples:** Practical implementations of optimization algorithms for various scenarios, including code, results, and explanations.

Primary technologies and file types used:
* HTML (`.html`) for notes and descriptive pages.
* Python (`.py`) for coding exercises and simulations.
* MATLAB (`.m`, `.fig`) for coding exercises, simulations, and figure files.
* Images (`.png`, `.jpg`) for plots and visual results.

## Directory Structure

The repository is organized by chapters to align with the course structure. Here's a general overview:

- Optimization-Homework-Simulations/
├── .gitignore
├── README.md  (This file)
│
├── Chapter01/
│   ├── Notes/
│   │   └── notes_chapter01.html  (Learning notes for Chapter 1)
│   │
│   ├── Exercises/
│   │   ├── Ex1_TopicName/        (Folder for a specific exercise, e.g., Ex1_GradientDescent)
│   │   │   ├── index.html        (HTML write-up for the exercise: description, code, results)
│   │   │   ├── code_ex1.py       (Python code for the exercise)
│   │   │   ├── code_ex1.m        (MATLAB code for the exercise)
│   │   │   ├── output_ex1.png    (Image output from the code)
│   │   │   └── figure_ex1.fig    (MATLAB .fig file)
│   │   └── ... (Other exercises, each in its own sub-folder)
│   │
│   ├── Simulations/
│   │   ├── Sim1_ScenarioName/    (Folder for a specific simulation, e.g., Sim1_ConstrainedOpt)
│   │   │   ├── index.html        (HTML write-up for the simulation)
│   │   │   ├── code_sim1.py      (Python code for the simulation)
│   │   │   ├── code_sim1.m       (MATLAB code for the simulation)
│   │   │   ├── output_sim1.png   (Image output from the simulation)
│   │   │   └── figure_sim1.fig   (MATLAB .fig file)
│   │   └── ... (Other simulations, each in its own sub-folder)
│   │
│   └── README_Chapter01.md (Optional: Specific notes for Chapter 1)
│
├── Chapter02/
│   └── ... (Similar structure for subsequent chapters)
│
└── assets/  (Optional: Global assets like shared CSS or images)
└── css/

**Key points about the structure:**
* Each `ChapterXX/` folder corresponds to a chapter in the textbook.
* Inside each chapter:
    * `Notes/` contains general learning notes in HTML.
    * `Exercises/` contains solutions and code for homework problems. Each exercise is typically in its own sub-folder (e.g., `Ex1_TopicName/`) containing an `index.html` for explanation, code files (`.py`, `.m`), and output files (`.png`, `.fig`).
    * `Simulations/` contains practical simulation examples. Each simulation is typically in its own sub-folder (e.g., `Sim1_ScenarioName/`) with a similar structure to exercises.
* The `index.html` file within an exercise or simulation folder is the main entry point for that specific item, often embedding or linking to code and results.

---

# 最优化方法-习题与仿真

本仓库包含了《最优化计算方法》课程的学习资料。其中包括个人学习笔记、课后习题解答、以及相关的实例仿真，同时附有对应的代码（Python、MATLAB）和输出文件（图片、.fig 文件）。

## 关于此仓库

本项目是一个个人学习空间，致力于理解和应用最优化技术。所有材料均按照课程的章节结构进行组织。

主要内容包括：
* **学习笔记：** 基于 HTML 的笔记，总结了每个章节的关键概念。
* **课后习题：** 详细的课程习题解答和说明，通常附有 Python 或 MATLAB 代码及可视化输出。
* **实例仿真：** 针对不同场景的最优化算法的实践实现，包括代码、结果和解释。

使用的主要技术和文件类型：
* HTML (`.html`)：用于笔记和描述性页面。
* Python (`.py`)：用于编程练习和仿真。
* MATLAB (`.m`, `.fig`)：用于编程练习、仿真以及图形文件。
* 图片 (`.png`, `.jpg`)：用于图表和可视化结果。

## 目录结构

本仓库按章节组织，以与课程结构保持一致。以下是总体概览：

最优化方法-习题与仿真/

├── .gitignore
├── README.md  (当前文件)

│

├── Chapter01/ (第一章)

│   ├── Notes/ (笔记)

│   │   └── notes_chapter01.html  (第一章学习笔记)

│   │

│   ├── Exercises/ (课后习题)

│   │   ├── Ex1_主题名称/         (单个练习的文件夹，例如：Ex1_梯度下降法)

│   │   │   ├── index.html        (该练习的HTML说明文档：问题描述、代码、结果等)

│   │   │   ├── code_ex1.py       (该练习的Python代码)

│   │   │   ├── code_ex1.m        (该练习的MATLAB代码)

│   │   │   ├── output_ex1.png    (代码运行输出的图片)

│   │   │   └── figure_ex1.fig    (MATLAB .fig 文件)

│   │   └── ... (其他练习，每个在各自的子文件夹中)

│   │

│   ├── Simulations/ (实例仿真)

│   │   ├── Sim1_场景名称/        (单个仿真的文件夹，例如：Sim1_约束优化)

│   │   │   ├── index.html        (该仿真的HTML说明文档)

│   │   │   ├── code_sim1.py      (该仿真的Python代码)

│   │   │   ├── code_sim1.m       (该仿真的MATLAB代码)

│   │   │   ├── output_sim1.png   (代码运行输出的图片)

│   │   │   └── figure_sim1.fig   (MATLAB .fig 文件)

│   │   └── ... (其他仿真，每个在各自的子文件夹中)

│   │

│   └── README_Chapter01.md (可选：第一章内容的特定说明)

│

├── Chapter02/ (第二章)

│   └── ... (后续章节结构类似)

│

└── assets/  (可选：全局资源，如共享的CSS文件或图片)

└── css/

**关于结构的关键点：**
* 每个 `ChapterXX/` 文件夹对应教材中的一个章节。
* 在每个章节内部：
    * `Notes/` 包含通用的 HTML 学习笔记。
    * `Exercises/` 包含课后作业的解答和代码。每个练习通常放在其自己的子文件夹中（例如 `Ex1_主题名称/`），其中包含用于解释的 `index.html` 文件、代码文件（`.py`, `.m`）和输出文件（`.png`, `.fig`）。
    * `Simulations/` 包含实际的仿真示例。每个仿真通常也放在其自己的子文件夹中（例如 `Sim1_场景名称/`），结构与练习类似。
* 练习或仿真文件夹内的 `index.html` 文件是该特定项目的主要入口点，通常会嵌入或链接到代码和结果。
