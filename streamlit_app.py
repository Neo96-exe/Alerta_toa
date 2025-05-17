# streamlit_app.py

import streamlit as st
import pandas as pd
from datetime import datetime
import os
from extrator_toa import extrair_planilha_toa

# ========== CONFIGURAÇÃO ==========
st.set_page_config(page_title="AlertaTOA - Extração TOA", layout="centered")

# ========== INTERFACE ==========
st.title("📥 AlertaTOA - Extração de Relatórios TOA")

st.markdown("Preencha suas credenciais abaixo para iniciar a extração do relatório.")

login = st.text_input("Login", placeholder="Digite seu login Claro")
senha = st.text_input("Senha", type="password", placeholder="Digite sua senha")
oma = st.text_input("Código OMA", placeholder="Informe o código de autenticação (6 dígitos)")

if st.button("🔄 Extrair Planilha TOA"):
    if not login or not senha or not oma:
        st.warning("⚠️ Por favor, preencha todos os campos.")
    else:
        with st.spinner("Realizando extração, aguarde..."):
            sucesso, mensagem = extrair_planilha_toa(login, senha, oma)

            # Registrar no histórico
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            novo_log = pd.DataFrame([{
                "Data/Hora": now,
                "Login": login,
                "Status": "Sucesso" if sucesso else "Erro",
                "Mensagem": mensagem
            }])

            if os.path.exists("log_extracoes.csv"):
                log_antigo = pd.read_csv("log_extracoes.csv")
                log_completo = pd.concat([novo_log, log_antigo], ignore_index=True)
            else:
                log_completo = novo_log

            log_completo.to_csv("log_extracoes.csv", index=False)

            if sucesso:
                st.success("✅ Extração concluída com sucesso!")
            else:
                st.error(f"❌ Falha na extração: {mensagem}")

# ========== HISTÓRICO ==========
st.markdown("---")
st.subheader("📊 Histórico de Extrações")

if os.path.exists("log_extracoes.csv"):
    log_df = pd.read_csv("log_extracoes.csv")
    st.dataframe(log_df)
else:
    st.info("Nenhuma extração registrada até o momento.")
