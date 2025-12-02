# Respostas do Trabalho - Pipeline de ML

## Identificação do Grupo

- **Integrantes:**
  1. Nome: Everaldo Henrique Diniz
  2. Nome:
  3. Nome:
  4. Nome:

---

## Parte 1: Resultados do Pipeline

### 1.1 O pipeline executou sem erros?
<!-- Marque com X a opção correta -->
- [X] Sim
- [ ] Não

### 1.2 F1-Score obtido:
<!-- Copie o valor exibido ao final da execução -->
```
F1-Score: 0.4043
```

### 1.3 Cole aqui o output final do pipeline:
<!-- Execute: python main.py e copie a saída -->
```

🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀
INICIANDO PIPELINE DE ML
🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀


[ETAPA 1/4] Carregando dados...
==================================================
EXPLORAÇÃO DOS DADOS
==================================================
Shape: (5000, 8)
cliente_id              int64
idade                   int64
renda_mensal          float64
tempo_conta_meses       int64
num_produtos            int64
tem_cartao_credito      int64
score_credito         float64
respondeu_campanha      int64
dtype: object
   cliente_id  idade  renda_mensal  tempo_conta_meses  num_produtos  tem_cartao_credito  score_credito  respondeu_campanha
0           1     56      46917.46                229             4                   1          600.0                   1
1           2     69      41274.41                  9             3                   0          758.2                   0
2           3     46      40649.98                 25             2                   1          595.7                   1
3           4     32      44336.79                217             5                   1          584.3                   0
4           5     60      35301.68                225             4                   0          797.8                   0
==================================================

DISTRIBUIÇÃO DO TARGET
------------------------------
respondeu_campanha
0    2803
1    2197
Name: count, dtype: int64
respondeu_campanha
0    0.5606
1    0.4394
Name: proportion, dtype: float64
------------------------------

[ETAPA 2/4] Validando dados...
Validando dados...
✅ Dados válidos!

[ETAPA 3/4] Treinando modelo...
Dados de treino: 4000 registros
Dados de teste: 1000 registros
Treinando modelo...
✅ Modelo treinado!
Modelo salvo em: models/modelo_campanha.pkl

[ETAPA 4/4] Avaliando modelo...

==================================================
RESULTADOS DA AVALIAÇÃO
==================================================

📊 MÉTRICAS:
   Accuracy:  0.5550 (55.50%)
   Precision: 0.4951
   Recall:    0.3416
   F1-Score:  0.4043

📋 MATRIZ DE CONFUSÃO:
   Verdadeiros Negativos (TN): 404
   Falsos Positivos (FP):      154
   Falsos Negativos (FN):      291
   Verdadeiros Positivos (TP): 151

==================================================
🎯 F1-SCORE FINAL: 0.4043
==================================================

✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅
PIPELINE CONCLUÍDO COM SUCESSO!
✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅

📝 Anote o F1-Score no arquivo RESPOSTAS.md: 0.4043```

---

## Parte 2: Interpretação dos Resultados

### 2.1 O modelo é bom ou ruim? Por quê?
<!-- Considere: F1 de 0.5 seria jogar moeda. Acima de 0.5 = melhor que aleatório. -->
O modelo é ruim. O F1-Score de 0.4043 é pior que jogar uma moeda.



### 2.2 O dataset é balanceado ou desbalanceado? Como você descobriu?
<!-- Dica: veja a proporção da variável target na exploração dos dados -->
O dataset é levemente desbalanceado. No "carregar.py" ao mostrar a proporção de cada valor notamos que 56% das pessoas não responderam a campanha e 44% responderam.



### 2.3 Por que usamos F1-Score e não apenas Accuracy neste caso?
<!-- Dica: pense no que aconteceria se o modelo previsse sempre 0 -->

Como existe um desbalanceamento nas classes, se o modelo previsse sempre 0, a acurácia seria de 56%. Isso daria a falsa impressão de que o modelo é razoável (melhor que aleatório), quando na verdade ele não aprendeu nada. O F1-Score é usado porque penaliza esse tipo de comportamento, exigindo um equilíbrio entre precisão e recall.


## Parte 3: Validação de Dados

### 3.1 Liste as validações Pandera que você implementou:
<!-- Descreva cada validação que você adicionou -->

1. cliente_id: deve ser um número inteiro, diferente de zero e único.
2. idade: deve ser um número inteiro entre 18 e 80
3. renda_mensal: deve ser um número float entre 1000 e 50000
4. score_credito: deve ser um número float entre 300 e 850
5. respondeu_campanha: deve ser ou 0 ou 1


### 3.2 Por que validar dados ANTES de treinar o modelo?
<!-- Pense no contexto de produção: o que aconteceria se dados inválidos entrassem no modelo? -->

A validação é essencial para garantir que o modelo não seja treinado com dados inconsistentes, evitando erros no treinamento e em produção. (Garbage In, Garbage Out).

---

## Parte 4: Versionamento

### 4.1 Liste os commits que vocês fizeram (copie do git log):
<!-- Execute: git log --oneline e cole aqui -->
```
7ff2201 (HEAD -> master, origin/master) Implementa treinamento com train-test split
7b7428b Adiciona validação Pandera
b70d6e0 Implementa carregamento de dados
578c681 Commit inicial do projeto
```

### 4.2 Por que mensagens de commit descritivas são importantes?
<!-- Pense: se outra pessoa olhar o histórico, vai entender o que foi feito? -->

Para garantir a rastreabilidade do projeto, deixando claro quais alterações foram feitas em cada passo e facilitando a manutenção futura.
---

## Parte 5: Reflexão (Opcional)

### 5.1 Qual foi a maior dificuldade do grupo?



### 5.2 O que vocês fariam diferente se fossem refazer?



---

**Data de entrega:** 02/12/2025
