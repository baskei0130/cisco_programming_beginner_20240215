# Cisco Programming Beginner

本レポジトリは、2024年2月15日に実施したAPI/Programmability入門における
「20240215_CiscoSEによるAPI-プログラマビリティ実践part1」の実施内容です。

## 概要
Cisco Modeling Labs (CML) 上に構築したLabに対し、
ChatGPTに作成してもらったpythonスクリプトでコンフィグの取得、インタフェースをshutdown、検証の自動化を実施しました。

## フォルダ説明
以下に本レポジトリ内にあるフォルダを示します。
各フォルダには詳細を説明するReadme、Pythonスクリプト、CMLでLabを構築するためのYAMLファイルがあります。
- get-run-cfg
  - running-configを取得します
- change-if-down
  - あるインタフェースをshutdownします
- vpc-test-pyats
  - vPCの検証を自動化します