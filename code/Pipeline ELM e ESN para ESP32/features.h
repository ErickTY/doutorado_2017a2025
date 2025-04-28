// features.h - Lista de features selecionadas para inferência
// Este arquivo contém os nomes das 10 features mais importantes escolhidas após o treinamento
// para serem utilizadas no pré-processamento e normalização no ESP32.

#ifndef FEATURES_H
#define FEATURES_H

const char* features[10] = {
    "0_MFCC_3",
    "0_MFCC_4",
    "0_Negative turning points",
    "0_MFCC_2",
    "0_ECDF Percentile_1",
    "0_Max",
    "0_Entropy",
    "0_Mean absolute deviation",
    "0_Kurtosis",
    "0_Median absolute deviation"
};

#endif // FEATURES_H
