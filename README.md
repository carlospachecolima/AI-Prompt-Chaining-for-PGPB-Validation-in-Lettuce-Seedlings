AI-Prompt-Chaining-for-PGPB-Validation-in-Lettuce-Seedlings

This repository contains the source code, prompt engineering methodology, and technical documentation for an AI-assisted visual validation framework applied to Plant Growth-Promoting Bacteria (PGPB) in lettuce (Lactuca sativa L.) seedling production.

Related scientific publication
The results obtained using this framework are published in:
> Fontenelle, M. R.; Silva, K. M. N. B.; Silva, K. C. R.; Rodrigues, G. S. S.;  
> Jorge, M. H. A.; Lima, C. E. P.  
> **Plant Growth-Promoting Bacteria and Generative AI Validation in Sustainable Lettuce Seedling Production Systems**.  
> *Revista de Derecho y Cambio Social*, v. 22, p. 1–24, 2025.  
> DOI: https://doi.org/10.54899/dcs.v22i83.3634  
> Available at: https://ojs.revistadcs.com/index.php/revista/article/view/3634/2782

The workflow applies **Prompt Chaining** to integrate:
- Expert persona emulation,
- Structured visual analysis,
- Human-quality filtering (uniformity of stand),
- Quantitative ranking integration.

Repository structure
- `src/` – Python source code
- `docs/` – Technical and methodological documentation (LEPD)
- `tools/` – Auxiliary scripts (e.g., SHA-256 hash generation)

How it works
1. Two production cycles are visually analyzed using chained prompts.
2. Treatments (T1–T12) are ranked based on color, uniformity, and physiological disorders.
3. Visual rankings are integrated with quantitative rankings from experimental data.
4. Only treatments meeting **human visual quality criteria** are considered valid.

How to run
```bash
python src/main_pgpb_analise.py
Citation
Citation

Please cite this repository using the Zenodo DOI provided in the Releases section.

License

BSD 3-Clause License.

