import streamlit as st

valid_bases = {'A', 'T', 'G', 'C'}

st.title("🧬 DNA Mutation Finder")

seq1 = st.text_area("Enter First DNA Sequence").upper()
seq2 = st.text_area("Enter Second DNA Sequence").upper()

if st.button("Find Mutations"):
    if not seq1 or not seq2:
        st.error("Please enter both sequences.")
    elif any(base not in valid_bases for base in seq1):
        st.error("Invalid character in first sequence.")
    elif any(base not in valid_bases for base in seq2):
        st.error("Invalid character in second sequence.")
    else:
        st.subheader("Results:")
        min_len = min(len(seq1), len(seq2))
        differences_found = False

        for i in range(min_len):
            if seq1[i] != seq2[i]:
                st.write(f"🔺 Position {i+1}: {seq1[i]} → {seq2[i]}")
                differences_found = True

        if len(seq1) != len(seq2):
            st.warning("Note: Sequences are of different lengths.")
            differences_found = True

        if not differences_found:
            st.success("Sequences are identical within compared length.")
