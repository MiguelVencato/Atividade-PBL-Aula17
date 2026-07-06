Markdown# Atividade PBL - Aula 17: Qualidade de Software

**Integrantes:** Janine Veigas Farias e Miguel Rubim Vencato

## 1. Repositório da Atividade

| Item | Descrição |
| :--- | :--- |
| **Nome do repositório** | Atividade-PBL-Aula17 |
| **Link do repositório** | [https://github.com/MiguelVencato/Atividade-PBL-Aula17](https://github.com/MiguelVencato/Atividade-PBL-Aula17) |

**Estrutura de diretórios:**
<img width="380" height="312" alt="image" src="https://github.com/user-attachments/assets/b0b57db4-df0b-491f-84c2-0b5b3159c74c" />

2. Planejamento da FuncionalidadeItemDescriçãoTítulo da IssueImplementar cálculo de total de pedidoObjetivoGarantir o cálculo correto do preço total de itens.Link da IssueLink da Issue #13. Teste AutomatizadoItemDescriçãoTipo de testeUnitárioObjetivoValidar cálculo de valores positivos e negativosLink do arquivotest_order.pyCódigo do teste:Pythonfrom src.order import calcular_total

def test_calcular_total_valido():
    assert calcular_total(10.0, 2) == 20.0

def test_calcular_total_negativo():
    assert calcular_total(-10, 2) == 0
4. Pipeline de Integração ContínuaItemDescriçãoNome do workflowCI Quality PipelineEvento de disparoPush na branch mainLink do workflowquality.ymlLink da execuçãoExecução #3Evidência de sucesso (Pipeline Verde):5. Indicadores de QualidadeIndicadorValorQuantidade de testes executados2Quantidade de testes aprovados2Quantidade de testes com falha0Status final do pipelineSucesso6. Registro de DefeitoItemDescriçãoTítulo do defeitoErro na fórmula de cálculo do totalSeveridadeAltaLink da Issue[COLE AQUI O LINK DA NOVA ISSUE DE BUG]Descrição:O defeito foi introduzido propositalmente alterando a lógica de cálculo. Foi identificado automaticamente pelo pipeline (falha no pytest). A correção foi realizada revertendo o código para a lógica original.
