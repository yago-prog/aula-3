import json

def calcular_renda_mensal():
    # Solicita ao usuário a quantidade de aulas e valor pago por hora para cada tipo de aula
    aulas_cursos_principais = int(input("Quantidade de aulas de cursos principais no mês: "))
    aulas_workshops = int(input("Quantidade de workshops no mês: "))
    aulas_super_modulos = int(input("Quantidade de super módulos no mês: "))

    valor_hora_cursos_principais = float(input("Valor pago por hora para cursos principais: "))
    valor_hora_workshops = float(input("Valor pago por hora para workshops: "))
    valor_hora_super_modulos = float(input("Valor pago por hora para super módulos: "))

    # Duração de cada tipo de aula em horas
    duracao_cursos_principais = 3.5
    duracao_workshops = 2
    duracao_super_modulos = 3

    # Cálculo de horas e rendas para cada tipo de aula
    horas_totais_cursos_principais = aulas_cursos_principais * duracao_cursos_principais
    renda_cursos_principais = horas_totais_cursos_principais * valor_hora_cursos_principais

    horas_totais_workshops = aulas_workshops * duracao_workshops
    renda_workshops = horas_totais_workshops * valor_hora_workshops

    horas_totais_super_modulos = aulas_super_modulos * duracao_super_modulos
    renda_super_modulos = horas_totais_super_modulos * valor_hora_super_modulos

    # Cálculo das horas totais trabalhadas e da renda total
    total_horas_trabalhadas = horas_totais_cursos_principais + horas_totais_workshops + horas_totais_super_modulos
    renda_total = renda_cursos_principais + renda_workshops + renda_super_modulos

    # Estrutura de saída JSON
    resultado = {
        "total_horas_trabalhadas": total_horas_trabalhadas,
        "renda_total": renda_total,
        "detalhes": {
            "cursos_principais": {
                "aulas": aulas_cursos_principais,
                "horas_totais": horas_totais_cursos_principais,
                "renda": renda_cursos_principais
            },
            "workshops": {
                "aulas": aulas_workshops,
                "horas_totais": horas_totais_workshops,
                "renda": renda_workshops
            },
            "super_modulos": {
                "aulas": aulas_super_modulos,
                "horas_totais": horas_totais_super_modulos,
                "renda": renda_super_modulos
            }
        }
    }

    # Converte o resultado para JSON e imprime
    print(json.dumps(resultado, indent=4))

# Chama a função para executar o cálculo
calcular_renda_mensal()
