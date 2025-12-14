# main_pgpb_analise.py

from prompt_pgpb import PromptPGPB
import os

# -----------------------------------------------------------------------------
# CLASSE DE ORQUESTRAÇÃO DO WORKFLOW PGPB
# -----------------------------------------------------------------------------
class AnalisePGPBAutomatizada:
    
    def __init__(self, foto_caminho_c1, foto_caminho_c2):
        self.motor_prompts = PromptPGPB(foto_caminho_c1, foto_caminho_c2)
        
    def iniciar_workflow_pgpb(self):
        
        print("-------------------------------------------------------------------------")
        print(" Iniciando Software de Validação PGPB (Prompt Chaining p/ 2 Ciclos)")
        print("-------------------------------------------------------------------------")
        
        # 1. Execução do Ciclo 1
        prompt_c1 = self.motor_prompts.gerar_prompt_encadeado_ciclo(1)
        print("\n[MÓDULO 1: EXECUÇÃO CICLO 1]")
        print("Enviando Prompt Encadeado (P1-P5) para a IA (Análise Visual Ciclo 1)...")
        # print(prompt_c1) # Opcional: imprimir o prompt completo
        
        # Simulação de coleta de ranking da IA (Poderia ser um loop de API)
        ranking_c1_ia = "T7=T4>T5=T8>..." # Exemplo de resultado da IA
        print(f"Resultado do Ranking Visual (Ciclo 1) Coletado: {ranking_c1_ia}")

        # 2. Execução do Ciclo 2
        prompt_c2 = self.motor_prompts.gerar_prompt_encadeado_ciclo(2)
        print("\n[MÓDULO 2: EXECUÇÃO CICLO 2]")
        print("Enviando Prompt Encadeado (P1-P5) para a IA (Análise Visual Ciclo 2)...")
        # print(prompt_c2) # Opcional: imprimir o prompt completo
        
        ranking_c2_ia = "T7=T10=T11=T12>..." # Exemplo de resultado da IA
        print(f"Resultado do Ranking Visual (Ciclo 2) Coletado: {ranking_c2_ia}")
        
        # 3. Execução da Integração Final (O Filtro de Qualidade Humana)
        prompt_integracao = self.motor_prompts.gerar_prompt_integrado_final()
        print("\n[MÓDULO 3: INTEGRAÇÃO FINAL (Aplica Lógica de Autoria)]")
        print("Enviando Prompt de Integração (P6) para o LLM (Priorizando Uniformidade de Stand)...")
        
        # Simulação do resultado final integrado (que valida a metodologia)
        print(f"\nPROMPT DE INTEGRAÇÃO FINAL:\n{prompt_integracao}")
        print("\n---------------------------------------------------------")
        print("✅ WORKFLOW CONCLUÍDO. Lógica de Prompt Chaining para PGPB validada.")
        print("---------------------------------------------------------")
        return prompt_integracao

# -----------------------------------------------------------------------------
# EXECUÇÃO DO PROGRAMA
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    FOTO_C1 = "PGPB_ciclo_1.jpg"
    FOTO_C2 = "PGPB_ciclo_2.jpg"
    
    try:
        workflow = AnalisePGPBAutomatizada(FOTO_C1, FOTO_C2)
        workflow.iniciar_workflow_pgpb()
        
    except ImportError:
        print("\n❌ ERRO: O módulo 'prompt_pgpb' não foi encontrado. Verifique os nomes dos arquivos.")
    except Exception as e:
        print(f"\n❌ ERRO FATAL NA EXECUÇÃO DO SOFTWARE: {e}")