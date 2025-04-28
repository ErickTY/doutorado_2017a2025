// normalization.h - Médias e desvios padrão para normalização z-score
// Este arquivo contém os vetores usados para normalizar as features extraídas de cada janela de dados.

#ifndef NORMALIZATION_H
#define NORMALIZATION_H

// Vetor de médias para as 10 features selecionadas
const float feature_means[10] = {
    0.015, // 0_MFCC_3
    0.020, // 0_MFCC_4
    5.312, // 0_Negative turning points
    0.018, // 0_MFCC_2
    45.7,  // 0_ECDF Percentile_1
    6.85,  // 0_Max
    2.11,  // 0_Entropy
    0.89,  // 0_Mean absolute deviation
    3.02,  // 0_Kurtosis
    0.75   // 0_Median absolute deviation
};

// Vetor de desvios padrão para as 10 features selecionadas
const float feature_stds[10] = {
    0.012, // 0_MFCC_3
    0.015, // 0_MFCC_4
    2.89,  // 0_Negative turning points
    0.011, // 0_MFCC_2
    25.4,  // 0_ECDF Percentile_1
    2.15,  // 0_Max
    0.35,  // 0_Entropy
    0.28,  // 0_Mean absolute deviation
    1.45,  // 0_Kurtosis
    0.24   // 0_Median absolute deviation
};

#endif // NORMALIZATION_H
