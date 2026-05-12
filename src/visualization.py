from __future__ import annotations
"""
Funzioni di visualizzazione condivise per il progetto student-dropout-ml.

Contiene plot e helper riutilizzabili tra i diversi notebook del progetto.
Ogni funzione è auto-documentata e progettata per essere chiamata da più US
senza dipendenze esterne dai notebook.
"""

import math

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.ticker import MultipleLocator


# =============================================================================
# Costanti del modulo
# =============================================================================

# Label leggibili per le variabili del dataset.
# Estendibile dai notebook tramite il parametro `display_names_override`
# di plot_numeric_by_target.
DEFAULT_DISPLAY_NAMES = {
    'previous_qualification_grade':  'Voto della qualifica precedente',
    'admission_grade':               'Voto di ammissione',
    'age_at_enrollment':             "Età all'iscrizione",
    'cu_1st_sem_approved':           'Esami superati al 1° semestre',
    'cu_2nd_sem_approved':           'Esami superati al 2° semestre',
    'cu_1st_sem_grade':              'Voto medio al 1° semestre',
    'cu_2nd_sem_grade':              'Voto medio al 2° semestre',
    'inflation_rate':                'Tasso di inflazione (%)',
}

# Palette colori standard per il confronto Dropout vs Graduate.
# Dodger Blue (chiaro) per Dropout, Navy (scuro) per Graduate.
DEFAULT_PALETTE = {
    'Dropout':  '#1e90ff',
    'Graduate': '#07004d',
}


# =============================================================================
# Funzioni di plotting
# =============================================================================

def plot_numeric_by_target(
    df: pd.DataFrame,
    column: str,
    target_col: str = 'target',
    target_labels: dict | None = None,
    display_names_override: dict | None = None,
    bin_width: float | None = None,
    xtick_step: int | None = 10,
    xticks_custom: list | None = None,
    xlim: tuple | None = None,
    ylim: tuple | None = None,
    xlabel: str | None = None,
    ylabel: str = 'Densità',
    title: str | None = None,
    figsize: tuple = (9, 5),
):
    """
    Plotta la distribuzione di una variabile numerica separata per classe target.

    Usa un istogramma con sovrapposizione semitrasparente (`multiple='layer'`)
    e densità normalizzata per gruppo (`stat='density', common_norm=False`),
    pensato per confrontare distribuzioni di gruppi di dimensioni diverse.

    Parameters
    ----------
    df : pd.DataFrame
        Il dataset contenente la variabile e la colonna target.
    column : str
        Nome della colonna numerica da plottare sull'asse X.
    target_col : str, default 'target'
        Nome della colonna target binaria (0/1) nel df.
    target_labels : dict, optional
        Mapping da valore numerico a etichetta leggibile per la legenda.
        Default: {0: 'Dropout', 1: 'Graduate'}.
    display_names_override : dict, optional
        Dizionario di label aggiuntive o sostitutive rispetto a
        `DEFAULT_DISPLAY_NAMES`. Le chiavi presenti qui hanno la precedenza
        sui default. Permette di estendere il modulo senza modificarlo.
    bin_width : float, optional
        Larghezza fissa dei bin dell'istogramma. Accetta sia interi che
        decimali (es. 0.5 per voti scala 0-20, 5 per voti scala 0-200).
        Se None, usa auto-detection (1 bin per valore distinto se la colonna
        è intera con <=50 valori distinti, altrimenti la regola di
        Freedman-Diaconis).
    xtick_step : int, default 10
        Passo fisso tra i tick dell'asse X. Ignorato se `xticks_custom`
        è specificato.
    xticks_custom : list, optional
        Lista di valori custom per i tick dell'asse X. Se specificata,
        sostituisce `xtick_step`.
    xlim : tuple, optional
        Tupla (min, max) per fissare i limiti dell'asse X. Utile per
        allineare visivamente grafici di variabili con range simili.
    ylim : tuple, optional
        Tupla (min, max) per fissare i limiti dell'asse Y. Utile per
        coppie di grafici che devono essere visualmente confrontabili.
    xlabel : str, optional
        Label dell'asse X. Se None, usa il nome leggibile della colonna
        (dai display names o Title Case automatico del nome originale).
    ylabel : str, default 'Densità'
        Label dell'asse Y.
    title : str, optional
        Titolo del grafico. Se None, usa il default generato dal nome
        leggibile della colonna.
    figsize : tuple, default (9, 5)
        Dimensioni della figura in pollici (larghezza, altezza).

    Returns
    -------
    matplotlib.figure.Figure
        L'oggetto figura, utile per salvare il grafico su file.

    Notes
    -----
    Assume che `df[column]` non contenga NaN (gestione a monte, US-05).
    """
    # Default mutabili gestiti dentro la funzione (anti-pattern evitarli in firma)
    if target_labels is None:
        target_labels = {0: 'Dropout', 1: 'Graduate'}

    # Costruzione del dizionario delle label leggibili:
    # parte dai default del modulo, poi sovrascrive/estende con l'override
    display_names = dict(DEFAULT_DISPLAY_NAMES)
    if display_names_override is not None:
        display_names.update(display_names_override)

    # Lista ordinata dei label, per fissare l'ordine di legenda
    label_order = [target_labels[0], target_labels[1]]

    # Mapping dei valori target nelle label leggibili (Serie temporanea)
    label_series = df[target_col].map(target_labels)

    # Calcolo dei bin
    if bin_width is not None:
        # Bin di larghezza fissa allineati a multipli di bin_width.
        # math.floor gestisce correttamente valori negativi.
        col_min = df[column].min()
        col_max = df[column].max()
        bin_start = math.floor(col_min / bin_width) * bin_width
        bin_end = (math.floor(col_max / bin_width) + 1) * bin_width
        # numpy.arange supporta passi decimali (range no);
        # +bin_width/2 garantisce inclusione di bin_end
        bins = list(np.arange(bin_start, bin_end + bin_width / 2, bin_width))
    else:
        # Auto-detection: per interi con pochi valori distinti, 1 bin per valore
        if pd.api.types.is_integer_dtype(df[column]):
            n_unique = df[column].nunique()
            bins = n_unique if n_unique <= 50 else 'auto'
        else:
            bins = 'auto'

    # Costruzione della figura
    fig, ax = plt.subplots(figsize=figsize)

    sns.histplot(
        data=df,
        x=column,
        hue=label_series,
        hue_order=label_order,
        palette=DEFAULT_PALETTE,
        multiple='layer',
        stat='density',
        common_norm=False,
        bins=bins,
        ax=ax,
    )

    # Risoluzione del nome leggibile della colonna
    pretty_column = display_names.get(
        column,
        column.replace('_', ' ').title(),
    )

    # Titolo e label
    ax.set_title(
        title if title else f'{pretty_column} — distribuzione per classe target',
        fontsize=13,
        pad=12,
    )
    ax.set_xlabel(xlabel if xlabel else pretty_column)
    ax.set_ylabel(ylabel)
    ax.grid(axis='y', alpha=0.3)

    # Tick X: lista custom o passo fisso (mutuamente esclusivi)
    if xticks_custom is not None:
        ax.set_xticks(xticks_custom)
    else:
        ax.xaxis.set_major_locator(MultipleLocator(xtick_step))

    # Limiti opzionali sugli assi
    if xlim is not None:
        ax.set_xlim(xlim)
    if ylim is not None:
        ax.set_ylim(ylim)

    # Fix legenda: seaborn a volte non popola le label quando hue è una Serie.
    # Recuperiamo i patches disegnati e costruiamo la legenda a mano.
    handles = ax.get_legend().legend_handles if ax.get_legend() else []
    if handles:
        ax.legend(
            handles=handles,
            labels=label_order,
            title='Outcome',
            loc='upper right',
        )

    plt.tight_layout()
    return fig