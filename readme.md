# 🤖 Assistente de Análise de Crédito Inteligente

Este projeto é uma solução de avaliação para o desafio do Banese Labs, com o objetivo de otimizar o processo de análise de crédito para pequenas e médias empresas (PMEs) utilizando IA Generativa.

O assistente foi desenvolvido para:
* **Sintetizar** informações financeiras e contextuais de diversas fontes de dados.
* **Identificar** riscos e oportunidades de forma proativa.
* **Gerar** recomendações preliminares para a concessão ou recusa de crédito.
* **Simular** cenários hipotéticos de forma interativa.

A solução é composta por um agente de IA em Python com uma interface web amigável, capaz de processar dados em múltiplos formatos e interagir com um modelo de linguagem para gerar análises inteligentes.

## 🚀 Arquitetura da Solução

O sistema é modular e dividido em camadas, garantindo escalabilidade e manutenibilidade.

![Diagrama da Arquitetura](https://i.imgur.com/G4xK8Wp.png)

* **Interface (Streamlit):** Uma aplicação web simples e intuitiva que permite ao usuário interagir com o assistente, carregar arquivos e visualizar as análises.
* **Backend (Python Agent):** A lógica de negócio do assistente. É responsável por orquestrar o fluxo de trabalho, processar os dados e se comunicar com o modelo de IA.
* **Modelo de IA (Google Gemini API):** O modelo de IA Generativa que realiza a análise de texto e gera as recomendações de crédito com base nos dados fornecidos.
* **Fontes de Dados:** O assistente é capaz de processar dados em quatro formatos diferentes, garantindo flexibilidade: **CSV**, **JSON**, **XML** e **Parquet**.

## 🛠️ Instalação e Uso

Siga os passos abaixo para rodar o projeto em seu ambiente local.

### **Pré-requisitos**

* Python 3.8 ou superior.
* Uma chave de API do Google Gemini. Você pode obtê-la no [Google AI Studio](https://ai.google.dev/).

### **Passo 1: Clone o Repositório**