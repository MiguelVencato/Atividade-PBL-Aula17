Markdown# Atividade PBL - Aula 17: Qualidade de Software

**Integrantes:** Janine Veigas Farias e Miguel Rubim Vencato

## 1. Repositório da Atividade

| Item | Descrição |
| :--- | :--- |
| **Nome do repositório** | Atividade-PBL-Aula17 |
| **Link do repositório** | [https://github.com/MiguelVencato/Atividade-PBL-Aula17](https://github.com/MiguelVencato/Atividade-PBL-Aula17) |
**Estrutura de diretórios:**

<img width="380" height="312" alt="image" src="https://github.com/user-attachments/assets/b0b57db4-df0b-491f-84c2-0b5b3159c74c" />



## 2. Planejamento da Funcionalidade

| Item | Descrição |
|---|---|
| **Título da Issue** | Implementar cálculo de total de pedido |
| **Objetivo** | Garantir o cálculo correto do preço total de itens. |
| **Link da Issue** | [Link da Issue #1](https://github.com/MiguelVencato/Atividade-PBL-Aula17/issues/1) |

## 3. Testes Unitários

```python
def test_calcular_total_valido():
    assert calcular_total(10.0, 2) == 20.0

def test_calcular_total_negativo():
    assert calcular_total(-10, 2) == 0
```
## 4. Pipeline de Integração Contínua

| Item | Descrição |
|---|---|
| **Nome do workflow** | CI Quality Pipeline |
| **Evento de disparo** | Push na branch main |
| **Link do workflow** | [quality.yml](https://github.com/MiguelVencato/Atividade-PBL-Aula17/blob/main/.github/workflows/quality.yml) |
| **Link da execução** | Execução #3 |
<img width="1351" height="175" alt="image" src="https://github.com/user-attachments/assets/0a0ee998-5d51-4b96-a786-cd74b6d771ce" />

5. Indicadores de QualidadeIndicadorValorQuantidade de testes executados2Quantidade de testes aprovados2Quantidade de testes com falha0Status final do pipelineSucesso6. Registro de DefeitoItemDescriçãoTítulo do defeitoErro na fórmula de cálculo do totalSeveridadeAltaLink da Issue[COLE AQUI O LINK DA NOVA ISSUE DE BUG]Descrição:O defeito foi introduzido propositalmente alterando a lógica de cálculo. Foi identificado automaticamente pelo pipeline (falha no pytest). A correção foi realizada revertendo o código para a lógica original.
