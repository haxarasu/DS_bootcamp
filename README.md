# DS_bootcamp

Кластер проектов для знакомства с **Python**, **Data Science** и **Machine Learning**: от базового Python и работы с данными до первых моделей и оценки качества. Репозиторий разбит по дням `DS_bootcamp.day00…day09`.

## Содержание (по модулям)
- **day00–day02** — основы Python, работа с файлами, `numpy`, `pandas`
- **day03** — EDA: первичный анализ данных, базовая чистка
- **day04** — визуализация (`matplotlib`/`plotly`)
- **day05–day06** — подготовка признаков, разделение на train/test
- **day07–day08** — первые модели (`scikit-learn`): линейные/деревья, метрики
- **day09** — итоговая сборка пайплайна
---

## Сборка
MacOS
```bash
python3 -m venv .venv
source .venv/bin/activate
```
Для установки пакетов:
```bash
pip3 install -r requirements.txt
```
Windows:
```bash
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
```
```bash
pip install -r requirements.txt
```
---
Запуск .py:
```bash
python file_name.py 
```
Запуск .ipynb через VS code:
Выбрать среду с установленными пакетами и нажать Run all