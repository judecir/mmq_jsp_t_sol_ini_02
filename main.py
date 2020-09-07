# Universidade Federal do Ceará
# Departamento de Estatística e Matemática Aplicada
# Mestrado em Modelagem e Métodos Quantitativos
# Aluno: Judecir Cavalcante (judecir@gmail.com)
# Orientador: Rafael Andrade (rca.ufc@gmail.com)
import os
import pandas as pd

#os.chdir("C:/Users/User/Google Drive/UFC/MMQ/PESQUISA/MODELO DO ARRANJO LINEAR MÍNIMO PARA JOB SHOP/CODIGOS/scripts")
#os.chdir("C:/Users/User/Documents/Python Scripts/teste_mmq_jsp_minla") 
  
from pre_processamento import criar_instancias

from resolucao import teste_manne_minlafav, teste_solucao_inicial

from pos_processamento import criar_df_comparacao,\
                                criar_tabela_layout_artigo

teste_solucao_inicial()

"""
inst_mod_pular = ["ID001_M015_J020_ZIntTrue_minla_fav", "ID008_M015_J020_ZIntTrue_minla_fav"]
prefixo_arq="t_nb_node"
df = teste_manne_minlafav(prefixo_arq, 
                          ini_amostra=0,
                          fim_amostra=2,
                          tempo_max=60,
                          fl_primeira_sol=False,
                          fl_heuristica_desabilitada=False,
                          inst_mod_pular=inst_mod_pular)

"""
"""
df_comp = criar_df_comparacao(df)

flags = 100*df_comp[["fl_funcao_objetivo",\
             "fl_best_bound", \
             "fl_mip_relative_gap", \
             "rel_fl_funcao_objetivo"]].sum()/df_comp["problema"].count()

print(" >>>>>>>>>> Resultados gerais: <<<<<<<<<<<<\n", flags)
df_comp.to_csv("solucoes/"+prefixo_arq+"_df_com"+".csv", index=False, sep=";", decimal=",")
"""

"""
lt, df = criar_tabela_layout_artigo(lista_nome_arquivo=["solucoes/sbpo/resultados_sbpo.csv"])

qtd_instancias = df.shape[0]
print("GAP Manne c/ desigualdades menor que Manne:")
qtd = (df["manne_desig - mip_relative_gap"] < df["manne - mip_relative_gap"]).sum()
print("Valor absoluto: ", qtd)
print("Percentual:", qtd/qtd_instancias*100)

print("RL Manne c/ desigualdades menor que Manne:")
qtd = (df["manne_desig - funcao_objetivo"] > df["manne - funcao_objetivo"])


print("GAP Liao c/ desigualdades menor que Liao:")
qtd = (df["liao_desig - mip_relative_gap"] < df["liao - mip_relative_gap"]).sum()
print("Valor absoluto: ", qtd)
print("Percentual:", qtd/qtd_instancias*100)

"""

"""
for i in lt:
    i["df"].to_csv("solucoes/sbpo/dados_"+i["modelo"]+".csv", index=False)
    print(i["modelo"])    

df = pd.merge(lt[0]["df"], lt[1]["df"], how="outer", on="problema")
df["ID"] = pd.to_numeric(df["problema"].str.slice(2,5))
df.drop(df.filter(regex='_y$').columns.tolist(),axis=1, inplace=True)
df.to_csv("solucoes/sbpo/dados_manne_m1.csv", index=False,decimal=',',sep=";", float_format='%.3f')

df = pd.merge(lt[2]["df"], lt[3]["df"], how="outer", on="problema")
df["ID"] = pd.to_numeric(df["problema"].str.slice(2,5))
df.drop(df.filter(regex='_y$').columns.tolist(),axis=1, inplace=True)
df.to_csv("solucoes/sbpo/dados_liao_l1.csv", index=False,decimal=',',sep=";", float_format='%.3f')
"""

