# K-Volei

> Projeto **acadêmico** da disciplina **Construções de Aplicações Orientadas a Objetos (CAOO)**.
> O K-Volei é um software em **Python** que usa **MVC**, **Cadeia de Responsabilidade** e **K-means** para, a partir de testes do PROESP realizado pela turma, **recomendar a posição no vôlei**: Levantador, Líbero, Central, Oposto ou Ponteiro.

## ✨ O que o projeto faz

* Importa um dataset com medidas físicas de alunos.
* Processa e padroniza os dados em um **pipeline** (CoR).
* Agrupa perfis com **K-means** (não supervisionado).
* Calcula **scores** por posição e gera uma **recomendação final**.
* Persiste alunos, clusters e recomendações em **MongoDB**.

## 🧱 Arquitetura (MVC + CoR)

* **Models**: entidades (Aluno, Medidas, Cluster, Recomendacao) e regras de domínio.
* **Views**: interface (CLI ou GUI simples) para importar dados, cadastrar aluno e ver resultados.
* **Controllers**: orquestram fluxo entre Views, Services e Repositórios.
* **CoR (pipeline)**: `Validate → Clean → Normalize → SelectFeatures → KMeans → Recommend`.

## 📊 Atributos esperados (exemplos)

* Peso, Altura em pé, Altura sentado
* Salto horizontal, Salto vertical
* Abdominais (1 min)
* Arremesso de medicine ball (2 kg)
* Sentar e alcançar

## 🧠 Como a recomendação funciona (resumo)

1. **Treino**: rodar K-means nas features padronizadas e salvar centróides/métricas.
2. **Inferência**: para cada aluno, achar o cluster mais próximo.
3. **Scoring por posição** (exemplo de diretrizes):

   * **Central**: Altura + Salto vertical
   * **Oposto**: Arremesso MB + Salto vertical
   * **Ponteiro**: Salto vertical + Salto horizontal + Flexibilidade
   * **Levantador**: Flexibilidade + Arremesso MB
   * **Líbero**: Flexibilidade + Salto horizontal
4. **Saída**: posição recomendada + justificativa (principais fatores).

## ⚙️ Requisitos

* Python **3.11+**
* `pip`/`venv`
* **MongoDB** local ou remoto

## 📦 Instalação

```bash
git clone https://github.com/seu-usuario/k-volei.git
cd k-volei
python -m venv .venv
# Windows: .venv\Scripts\activate
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

## 🔧 Configuração (.env)

```
# Mongo opcional: ajuste conforme seu ambiente
MONGODB_URI=mongodb://localhost:27017
DB_NAME=kvolei
```

---

> **Nota:** Este é um projeto acadêmico desenvolvido para a disciplina CAOO, com foco nos conceitos de POO, MVC, Cadeia de Responsabilidade e K-means.