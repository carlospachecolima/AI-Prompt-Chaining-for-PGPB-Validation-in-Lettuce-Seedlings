# prompt_pgpb.py

class PromptPGPB:
    """
    Define a metodologia de Prompt Chaining para a validação de IA em sistemas
    sustentáveis de produção de mudas (Foco em PGPB e qualidade de stand).
    """
    
    def __init__(self, caminho_foto_ciclo1, caminho_foto_ciclo2):
        self.caminho_foto_c1 = caminho_foto_ciclo1
        self.caminho_foto_c2 = caminho_foto_ciclo2
        self.total_tratamentos = 12 # T1 a T12
        
        # ----------------------------------------------------------------------
        # PROMPT 1: DEFINIÇÃO DA PERSONA E CONTEXTO MICROBIOLÓGICO [cite: 1056]
        # ----------------------------------------------------------------------
        self.P1_PERSONA = (
            "Assuma a persona de um Engenheiro Agrônomo com PhD em Microbiologia Agrícola e "
            "com pelo menos 15 anos de experiência em desenvolvimento e teste de bioinsumos e seus "
            "efeitos na fisiologia vegetal. Você deve avaliar o potencial de inoculantes bacterianos "
            "em promoção de crescimento de mudas de alface (Lactuca sativa L.)."
        )

        # ----------------------------------------------------------------------
        # PROMPT 2/3: ANÁLISE DO CICLO (Instrução de Observação e Contexto Científico) [cite: 1057, 1058]
        # ----------------------------------------------------------------------
        self.P2_ANALISECICLO = (
            "Analise cuidadosamente a foto anexada para o Ciclo de Produção. Tenha em mente que este é um experimento que "
            "avalia o desempenho de diferentes inoculantes microbianos (PGPB) com potencial de solubilização de fósforo e "
            "produção de sideróforos na produção de mudas de alface. (Tratamentos T1 a T12)."
        )

        # ----------------------------------------------------------------------
        # PROMPT 4: CRITÉRIOS DE AVALIAÇÃO VISUAL [cite: 1059]
        # Foco em uniformidade, que foi um fator chave na conclusão do artigo[cite: 1370].
        # ----------------------------------------------------------------------
        self.P4_CRITERIOS = (
            "Analise os seguintes padrões visuais nos tratamentos (T1 a T12): "
            "1. Intensidade da coloração verde; "
            "2. Uniformidade do stand das mudas; "
            "3. Presença de sinais de desordens fisiológicas (ex: clorose, queima de borda)."
        )

        # ----------------------------------------------------------------------
        # PROMPT 5: RANKING (Geração do dado primário visual) [cite: 1060]
        # ----------------------------------------------------------------------
        self.P5_RANKING = (
            "Com base nas observações feitas (Padrões 1, 2 e 3), classifique os 12 tratamentos do melhor para o pior "
            "para o ciclo em questão. (Melhor = 1ª posição, Pior = 12ª posição)."
        )
        
        # ----------------------------------------------------------------------
        # PROMPT 6: INTEGRAÇÃO FINAL (Aplica a lógica de exclusão/qualidade humana) [cite: 1071, 1072]
        # Esta etapa integra a análise qualitativa (visual) com a quantitativa (média de rank)
        # ----------------------------------------------------------------------
        self.P6_INTEGRACAO = (
            "Agora, combine o seu ranking visual para os dois ciclos com o ranking quantitativo médio fornecido pelos autores: "
            "T7(3.38), T5(4.12), T8(4.75), T12(5.00), T4(5.38), T9(5.50), T10(6.12), T6(6.50), T11(6.88), T1(7.75), T2(8.12), T3(10.12). "
            "O seu ranking final integrado deve priorizar a 'uniformidade do stand' vista visualmente. "
            "ATENÇÃO: Apenas considere como 'BONS TRATAMENTOS' aqueles que mostraram uniformidade no stand na análise visual, "
            "mesmo que tenham tido um bom ranking quantitativo (ex: T12 e T4 falharam na uniformidade visual humana). "
            "Gere o ranking final de T1 a T12 com base neste critério de integração."
        )

    def gerar_prompt_encadeado_ciclo(self, ciclo):
        """ Gera o prompt completo para um ciclo específico (P1 a P5). """
        if ciclo == 1:
            foto_path = self.caminho_foto_c1
        elif ciclo == 2:
            foto_path = self.caminho_foto_c2
        else:
            raise ValueError("Ciclo deve ser 1 ou 2.")
            
        return (
            f"--- ANÁLISE DO CICLO {ciclo} ---\n"
            f"{self.P1_PERSONA}\n\n"
            f"{self.P2_ANALISECICLO.replace('foto anexada', 'foto anexada para o Ciclo ' + str(ciclo))}\n\n"
            f"{self.P4_CRITERIOS}\n\n"
            f"{self.P5_RANKING}"
        )

    def gerar_prompt_integrado_final(self):
        """ Gera o prompt final de integração (P6), aplicando o filtro de qualidade (autoria intelectual). """
        return f"--- ETAPA FINAL DE INTEGRAÇÃO ---\n{self.P1_PERSONA}\n\n{self.P6_INTEGRACAO}"