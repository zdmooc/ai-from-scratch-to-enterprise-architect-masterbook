# V01 — Glossaire commun des fondamentaux IA

**Statut : DRAFT / revue scientifique et terminologique encore requise.** Les termes sont définis pour un lecteur débutant. Ils ne remplacent pas les définitions normatives, contractuelles ou juridiques applicables. Les renvois de type Cxx pointent vers les chapitres du volume.

- **Agent IA** — Application qui orchestre observations, états et éventuels outils autour d'une tâche; elle ne se confond pas avec le modèle utilisé. *Voir C08.*

- **Algorithme** — Suite définie d'opérations exécutables; il peut ne contenir aucun apprentissage. *Voir C01.*

- **Apprentissage non supervisé** — Recherche de structures ou représentations sans cible fournie à chaque observation. *Voir C04.*

- **Apprentissage supervisé** — Ajustement d'un modèle à partir d'observations accompagnées de cibles connues. *Voir C04.*

- **ASR** — Automatic Speech Recognition : transformation d'un signal de parole en transcription textuelle. *Voir C07.*

- **Attention** — Mécanisme calculant des poids de combinaison à partir de représentations numériques de séquence. *Voir C06.*

- **Autonomie bornée** — Capacité d'agir limitée par outils, permissions, budgets, état et contrôles effectifs. *Voir C08.*

- **Baseline** — Méthode de référence, souvent simple, utilisée pour juger un gain potentiel. *Voir C09/C11.*

- **Biais de données** — Différence ou déformation systématique introduite notamment par collecte, étiquetage ou population. *Voir C10.*

- **Calibration** — Concordance évaluée entre probabilités annoncées et fréquences effectivement observées. *Voir C04.*

- **Chaînage avant** — Application de règles partant de faits connus pour déduire de nouveaux faits jusqu'au point fixe. *Voir C03.*

- **Classification** — Prédiction d'une catégorie définie plutôt que d'une grandeur continue. *Voir C04.*

- **Contexte** — Informations effectivement transmises à une exécution de modèle, soumises à des limites de taille et de contrôle. *Voir C06.*

- **Corpus** — Ensemble identifié et gouverné de documents ou observations utilisés pour une tâche. *Voir C07.*

- **Critère éliminatoire** — Exigence dont l'échec rend une option inacceptable indépendamment d'un score composite. *Voir C09.*

- **Data leakage** — Utilisation d'une information indisponible au moment réel de la prédiction ou provenant indûment du test. *Voir C04/C11.*

- **Décision d'architecture (ADR)** — Document court exposant contexte, options, décision, raisons et conséquences. *Voir C09/C12.*

- **Deep Learning** — Sous-domaine du ML utilisant des réseaux de neurones à transformations successives. *Voir C05.*

- **Dérive** — Évolution des données ou de leurs relations pouvant dégrader les performances d'un système. *Voir C10.*

- **Données d'autorité** — Sources désignées responsables d'un type précis de fait; une synthèse IA ne les remplace pas. *Voir C12.*

- **Échantillon de test** — Données réservées à l'évaluation indépendante selon un protocole déclaré. *Voir C11.*

- **Embedding** — Vecteur numérique appris représentant une unité telle qu'un token, une phrase, une image ou un document. *Voir C06.*

- **Entraînement** — Procédure qui ajuste les paramètres d'un modèle à partir d'exemples ou d'autres signaux. *Voir C04/C05.*

- **Erreur absolue moyenne (MAE)** — Moyenne des valeurs absolues des écarts entre prédictions et observations, dans l'unité de la cible. *Voir C04/C11.*

- **Exigence fonctionnelle** — Description testable d'une fonction que le système doit réaliser. *Voir C12.*

- **Faux négatif** — Cas positif réel prédit comme négatif selon les définitions de la tâche. *Voir C04.*

- **Faux positif** — Cas négatif réel prédit comme positif selon les définitions de la tâche. *Voir C04.*

- **Feature** — Variable ou représentation d'entrée disponible au moment prévu pour la prédiction. *Voir C04.*

- **Fine-tuning** — Adaptation de paramètres préentraînés pour une tâche ou un comportement cible; détaillée dans V10. *Voir C06.*

- **Fonction de perte** — Mesure numérique de l'écart entre la sortie du modèle et l'objectif d'entraînement. *Voir C05.*

- **Génération** — Production de contenu à partir d'un modèle et d'un conditionnement, distincte de la recherche de documents. *Voir C07.*

- **Gradient** — Dérivées locales de la perte par rapport à des paramètres, utilisées par des optimiseurs. *Voir C05.*

- **Hallucination** — Contenu généré inexact ou non étayé, éventuellement présenté avec assurance. *Voir C07.*

- **HITL** — Human-in-the-Loop : intervention humaine habilitée dans certaines décisions ou étapes. *Voir C08/C10.*

- **Hyperparamètre** — Choix de configuration d'apprentissage ou d'architecture sélectionné hors de l'optimisation directe des poids. *Voir C05.*

- **Idempotence** — Propriété selon laquelle répéter une opération ne multiplie pas ses effets selon le contrat défini. *Voir C08.*

- **Inférence** — Utilisation d'un modèle entraîné sur une nouvelle entrée pour produire une sortie. *Voir C01/C05.*

- **Instruction non fiable** — Contenu externe qui doit être traité comme donnée et non comme autorité sur les politiques du système. *Voir C08.*

- **Jeu de validation** — Données servant à sélectionner modèle et hyperparamètres, distinctes du test final. *Voir C04.*

- **KV cache** — Stockage d'états de clés/valeurs accélérant certaines inférences autoregressives, avec coût mémoire. *Voir C06.*

- **Label** — Cible ou étiquette de référence associée à une observation dans un problème supervisé. *Voir C04.*

- **Latence P95** — Valeur de latence sous laquelle se situent environ 95 % des observations selon le périmètre et la méthode retenus. *Voir C01/C12.*

- **LLM** — Large Language Model : modèle de langage à grande capacité entraîné sur des séquences de tokens. *Voir C06.*

- **Machine Learning** — Famille de méthodes ajustant un modèle à partir de données ou de signaux d'apprentissage. *Voir C01/C04.*

- **MCP** — Model Context Protocol : protocole d'interaction entre des clients et serveurs d'outils/ressources, sans garantie d'autorisation implicite. *Voir C08.*

- **Métrique** — Quantité définie pour mesurer une propriété d'un système sur un protocole déclaré. *Voir C11.*

- **Multimodal** — Traite ou produit plusieurs modalités, par exemple texte, image et audio. *Voir C07.*

- **NFR** — Non-Functional Requirement : contrainte de qualité comme latence, sécurité, résilience ou coût. *Voir C01/C12.*

- **OCR** — Reconnaissance optique de caractères dans un document ou une image. *Voir C07.*

- **Point fixe** — État d'une déduction où une nouvelle application des règles ne produit aucun fait inédit. *Voir C03.*

- **Précision (classification)** — Part des alertes prédites positives qui correspondent réellement à des cas positifs. *Voir C04.*

- **Prompt** — Instructions et contenu transmis à un modèle; ne remplace jamais des contrôles côté API. *Voir C07.*

- **Prompt injection** — Tentative d'utiliser un contenu de moindre confiance pour changer les instructions ou actions autorisées. *Voir C08/C10.*

- **Q/K/V** — Query, Key, Value : projections de représentations numériques utilisées dans des mécanismes d'attention. *Voir C06.*

- **RAG** — Retrieval-Augmented Generation : récupération de sources puis génération conditionnée sur celles-ci. *Voir C07/C12.*

- **Rappel (classification)** — Part des cas positifs réels que le modèle a correctement signalés. *Voir C04.*

- **Règle métier** — Condition explicite définie et gouvernée pour une décision ou une transformation. *Voir C03.*

- **Requête autorisée** — Appel dont la cible, les paramètres et l'identité sont acceptés par le système de contrôle d'accès. *Voir C08.*

- **Résultat inconnu** — État où les observations ne permettent pas de confirmer succès ou échec d'une action. *Voir C08.*

- **Rétropropagation** — Calcul des gradients à travers les couches d'un réseau via la règle de chaîne. *Voir C05.*

- **Score composite** — Agrégation pondérée de critères, à interpréter avec conditions éliminatoires et hypothèses. *Voir C09.*

- **Série temporelle** — Suite d'observations indexées dans le temps, imposant une attention particulière aux fuites futures. *Voir C11.*

- **SLO** — Service Level Objective : objectif mesurable de service, à distinguer d'un résultat de test ponctuel. *Voir C01.*

- **Softmax** — Fonction normalisant un ensemble de scores réels en poids positifs sommant à 1. *Voir C06.*

- **Source de vérité** — Référentiel désigné comme autorité pour un fait dans le périmètre étudié. *Voir C12.*

- **Token** — Unité de découpage d'entrée/sortie définie par le tokenizer d'un modèle. *Voir C06.*

- **Transformer** — Famille d'architectures neuronales utilisant notamment des mécanismes d'attention. *Voir C06.*

- **TTS** — Text-to-Speech : production de signal vocal à partir de texte. *Voir C07.*

- **Zero Trust** — Approche de sécurité refusant une confiance implicite en raison de la seule position réseau; approfondie dans V18. *Voir C10.*

## Convention de rédaction

- Distinguer **fait**, **hypothèse**, **prédiction**, **réponse générée** et **action réellement observée**.
- Distinguer **source de vérité** et **contenu de contexte**.
- Utiliser **entraînement** pour l'ajustement des paramètres, **inférence** pour leur application.
- Ne pas qualifier une probabilité de **calibrée** sans mesure.
- Employer **DRAFT**, **DESIGN_ONLY**, **LOCAL_TEST_PASS**, **CI_PASS**, **RUNTIME_PROVEN** et **PUBLISHED** seulement avec les preuves correspondant à ces statuts.
- Pour les acronymes anglais, écrire la signification à la première apparition dans chaque chapitre destiné à être lu indépendamment.

**Nombre d'entrées : 69.** Ce glossaire fait partie du manuscrit et n'est pas encore un volume publié.
