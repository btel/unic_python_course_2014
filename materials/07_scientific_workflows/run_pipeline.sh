python batch_correlation.py data/*.txt
python merge_correlations.py results/lgn_session*.npz --save results/lgn_merged.npz
python merge_correlations.py results/v1_session*.npz --save results/v1_merged.npz
python plot_corr_coef.py results/v1_merged.npz results/lgn_merged.npz --save figures/compare_correlations.svg
