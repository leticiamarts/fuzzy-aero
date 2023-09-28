# pip install -U scikit-fuzzy
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
import skfuzzy as fuzz
import numpy as np

# Entrada:
frequencia = ctrl.Antecedent(np.arange(0, 8, 1), "frequencia")
tempo_disponivel = ctrl.Antecedent(np.arange(20, 91, 1), "tempo_disponivel")
excesso_peso = ctrl.Antecedent(np.arange(0, 41, 1), "excesso_peso")
adesao = ctrl.Antecedent(np.arange(0, 8, 1), "adesao")
condicionamento = ctrl.Antecedent(np.arange(16, 81, 1), "condicionamento")

# Saída:
intensidade = ctrl.Consequent(np.arange(30, 91, 1), "intensidade")

# Fuzzificação
# Entrada:
frequencia["baixa"] = fuzz.trapmf(frequencia.universe, [0, 0, 2, 4])
frequencia["moderada"] = fuzz.trimf(frequencia.universe, [2, 4, 6])
frequencia["alta"] = fuzz.trapmf(frequencia.universe, [4, 6, 7, 7])
tempo_disponivel["pouco"] = fuzz.trimf(tempo_disponivel.universe, [20, 20, 40])
tempo_disponivel["medio"] = fuzz.trimf(tempo_disponivel.universe, [30, 40, 50])
tempo_disponivel["muito"] = fuzz.trapmf(tempo_disponivel.universe, [40, 60, 90, 90])
excesso_peso["pouco"] = fuzz.trimf(excesso_peso.universe, [0, 0, 15])
excesso_peso["moderado"] = fuzz.trimf(excesso_peso.universe, [5, 15, 30])
excesso_peso["muito"] = fuzz.trapmf(excesso_peso.universe, [15, 30, 40, 40])
adesao["baixa"] = fuzz.trimf(adesao.universe, [0, 0, 3.5])
adesao["moderada"] = fuzz.trimf(adesao.universe, [0, 3.5, 7])
adesao["alta"] = fuzz.trimf(adesao.universe, [3.5, 7, 7])
condicionamento["baixo"] = fuzz.trapmf(condicionamento.universe, [16, 16, 20.5, 29.5])
condicionamento["baixo_medio"] = fuzz.trimf(
    condicionamento.universe, [20.5, 29.5, 38.5]
)
condicionamento["medio"] = fuzz.trimf(condicionamento.universe, [29.5, 38.5, 47.5])
condicionamento["medio_alto"] = fuzz.trapmf(
    condicionamento.universe, [38.5, 47.5, 56.5, 56.5]
)
condicionamento["alto"] = fuzz.trapmf(condicionamento.universe, [47.5, 56.5, 80, 80])

# Saída
intensidade["baixa"] = fuzz.trapmf(intensidade.universe, [30, 30, 37.5, 47.5])
intensidade["baixa_media"] = fuzz.trimf(intensidade.universe, [37.5, 47.5, 62.5])
intensidade["media"] = fuzz.trimf(intensidade.universe, [47.5, 62.5, 72.5])
intensidade["media_alta"] = fuzz.trimf(intensidade.universe, [62.5, 72.5, 85])
intensidade["alta"] = fuzz.trapmf(intensidade.universe, [72.5, 85, 90, 90])

# Inferência
regra1 = ctrl.Rule(condicionamento["alto"], intensidade["alta"])
regra2 = ctrl.Rule(condicionamento["medio_alto"], intensidade["media_alta"])
regra3 = ctrl.Rule(condicionamento["medio"], intensidade["media"])
regra4 = ctrl.Rule(condicionamento["baixo_medio"], intensidade["baixa_media"])
regra5 = ctrl.Rule(condicionamento["baixo"], intensidade["baixa"])
regra6 = ctrl.Rule(
    tempo_disponivel["muito"] & condicionamento["alto"], intensidade["media_alta"]
)
regra7 = ctrl.Rule(
    tempo_disponivel["muito"] & condicionamento["medio_alto"], intensidade["media"]
)
regra8 = ctrl.Rule(
    tempo_disponivel["muito"] & condicionamento["medio"], intensidade["baixa_media"]
)
regra9 = ctrl.Rule(frequencia["baixa"] & condicionamento["alto"], intensidade["alta"])
regra10 = ctrl.Rule(
    frequencia["baixa"] & condicionamento["medio_alto"], intensidade["alta"]
)
regra11 = ctrl.Rule(
    frequencia["baixa"] & condicionamento["medio"], intensidade["media_alta"]
)
regra12 = ctrl.Rule(
    frequencia["baixa"] & condicionamento["baixo_medio"], intensidade["media"]
)
regra13 = ctrl.Rule(
    frequencia["baixa"] & condicionamento["baixo"], intensidade["baixa_media"]
)
regra14 = ctrl.Rule(
    tempo_disponivel["pouco"] & condicionamento["alto"], intensidade["alta"]
)
regra15 = ctrl.Rule(
    tempo_disponivel["pouco"] & condicionamento["medio_alto"], intensidade["alta"]
)
regra16 = ctrl.Rule(
    tempo_disponivel["pouco"] & condicionamento["medio"], intensidade["media_alta"]
)
regra17 = ctrl.Rule(
    tempo_disponivel["pouco"] & condicionamento["baixo_medio"], intensidade["media"]
)
regra18 = ctrl.Rule(
    tempo_disponivel["pouco"] & condicionamento["baixo"], intensidade["baixa_media"]
)
regra19 = ctrl.Rule(
    frequencia["alta"] & condicionamento["alto"], intensidade["media_alta"]
)
regra20 = ctrl.Rule(
    frequencia["alta"] & condicionamento["medio_alto"], intensidade["media"]
)
regra21 = ctrl.Rule(
    frequencia["alta"] & condicionamento["medio"], intensidade["baixa_media"]
)
regra22 = ctrl.Rule(
    frequencia["alta"] & condicionamento["baixo_medio"], intensidade["baixa"]
)
regra23 = ctrl.Rule(adesao["alta"] & condicionamento["alto"], intensidade["alta"])
regra24 = ctrl.Rule(adesao["alta"] & condicionamento["medio_alto"], intensidade["alta"])
regra25 = ctrl.Rule(
    adesao["alta"] & condicionamento["medio"], intensidade["media_alta"]
)
regra26 = ctrl.Rule(
    adesao["alta"] & condicionamento["baixo_medio"], intensidade["media"]
)
regra27 = ctrl.Rule(
    adesao["alta"] & condicionamento["baixo"], intensidade["baixa_media"]
)
regra28 = ctrl.Rule(
    adesao["baixa"] & condicionamento["alto"], intensidade["media_alta"]
)
regra29 = ctrl.Rule(
    adesao["baixa"] & condicionamento["medio_alto"], intensidade["media"]
)
regra30 = ctrl.Rule(
    adesao["baixa"] & condicionamento["medio"], intensidade["baixa_media"]
)
regra31 = ctrl.Rule(
    adesao["baixa"] & condicionamento["baixo_medio"], intensidade["baixa"]
)
regra32 = ctrl.Rule(adesao["moderada"] & condicionamento["alto"], intensidade["alta"])
regra33 = ctrl.Rule(
    adesao["moderada"] & condicionamento["medio_alto"], intensidade["media_alta"]
)
regra34 = ctrl.Rule(adesao["moderada"] & condicionamento["medio"], intensidade["media"])
regra35 = ctrl.Rule(
    adesao["moderada"] & condicionamento["baixo_medio"], intensidade["baixa_media"]
)
regra36 = ctrl.Rule(adesao["moderada"] & condicionamento["baixo"], intensidade["baixa"])
regra37 = ctrl.Rule(
    excesso_peso["moderado"] & condicionamento["baixo"], intensidade["baixa_media"]
)
regra38 = ctrl.Rule(
    excesso_peso["moderado"] & condicionamento["baixo_medio"], intensidade["media"]
)
regra39 = ctrl.Rule(
    excesso_peso["moderado"] & condicionamento["medio"], intensidade["media_alta"]
)
regra40 = ctrl.Rule(
    excesso_peso["moderado"] & condicionamento["medio_alto"], intensidade["alta"]
)

intensidade_ctrl = ctrl.ControlSystem(
    [
        regra1,
        regra2,
        regra3,
        regra4,
        regra5,
        regra6,
        regra7,
        regra8,
        regra9,
        regra10,
        regra11,
        regra12,
        regra13,
        regra14,
        regra15,
        regra16,
        regra17,
        regra18,
        regra19,
        regra20,
        regra21,
        regra22,
        regra23,
        regra24,
        regra25,
        regra26,
        regra27,
        regra28,
        regra29,
        regra30,
        regra31,
        regra32,
        regra33,
        regra34,
        regra35,
        regra36,
        regra37,
        regra38,
        regra39,
        regra40,
    ]
)
intensidade_simulador = ctrl.ControlSystemSimulation(intensidade_ctrl)

### Simulação

intensidade_simulador.input["frequencia"] = 6  # 0 - 7
intensidade_simulador.input["tempo_disponivel"] = 28  # 20 - 90
intensidade_simulador.input["excesso_peso"] = 26  # 0 - 40
intensidade_simulador.input["adesao"] = 7  # 0 - 8
intensidade_simulador.input["condicionamento"] = 59  # 16 - 80

# Deffuzificação
intensidade_simulador.compute()
print(intensidade_simulador.output["intensidade"])
output_value = intensidade_simulador.output["intensidade"]
intensidade.view(sim=intensidade_simulador)
plt.savefig("intensidade2.png")
