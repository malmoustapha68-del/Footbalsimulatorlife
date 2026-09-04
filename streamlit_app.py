import streamlit as st
import random
from datetime import date, datetime

# ============================================================
# FOOTBALL LIFE SIMULATOR
# V1 - JEU COMPLET
# ============================================================

st.set_page_config(
    page_title="Football Life Simulator",
    page_icon="⚽",
    layout="wide"
)

# ------------------------------------------------------------
# CONFIGURATION
# ------------------------------------------------------------

NATIONALITES = [
    "Côte d'Ivoire",
    "France",
    "Sénégal",
    "Mali",
    "Cameroun",
    "Nigeria",
    "Ghana",
    "Maroc",
    "Algérie",
    "Brésil",
    "Argentine",
    "Espagne",
    "Angleterre"
]

POSTES = [
    "Gardien",
    "Défenseur",
    "Milieu",
    "Attaquant"
]

PIEDS = [
    "Droit",
    "Gauche"
]

CLUBS = [
    ("Abidjan FC", "Côte d'Ivoire", 48),
    ("ASEC Mimosas", "Côte d'Ivoire", 58),
    ("Africa Sports", "Côte d'Ivoire", 54),
    ("FC San Pedro", "Côte d'Ivoire", 56),
    ("Paris FC", "France", 62),
    ("Olympique Lyonnais", "France", 72),
    ("Marseille", "France", 76),
    ("Paris SG", "France", 88),
    ("Real Madrid", "Espagne", 92),
    ("FC Barcelona", "Espagne", 89),
    ("Manchester City", "Angleterre", 93),
    ("Liverpool", "Angleterre", 88),
    ("Arsenal", "Angleterre", 84),
    ("Bayern Munich", "Allemagne", 91),
    ("Inter Milan", "Italie", 84),
    ("AC Milan", "Italie", 80)
]


# ------------------------------------------------------------
# FONCTIONS
# ------------------------------------------------------------

def initialiser_jeu():
    """Crée une nouvelle partie vide."""
    st.session_state.jeu = {
        "cree": False,
        "prenom": "",
        "nom": "",
        "naissance": None,
        "nationalite": "",
        "poste": "",
        "pied": "",
        "club": "",
        "niveau_club": 0,
        "salaire": 0,
        "argent": 0,
        "saison": 2026,
        "semaine": 1,
        "forme": 70,
        "fatigue": 20,
        "moral": 70,
        "reputation": 10,
        "fans": 0,
        "niveau": 1,
        "experience": 0,
        "matchs": 0,
        "buts": 0,
        "passes": 0,
        "victoires": 0,
        "defaites": 0,
        "nuls": 0,
        "entrainements": 0,
        "journal": []
    }


def ajouter_journal(message):
    """Ajoute un événement à l'historique."""
    if "jeu" not in st.session_state:
        initialiser_jeu()

    st.session_state.jeu["journal"].insert(
        0,
        f"Saison {st.session_state.jeu['saison']} - "
        f"Semaine {st.session_state.jeu['semaine']} : {message}"
    )

    st.session_state.jeu["journal"] = (
        st.session_state.jeu["journal"][:100]
    )


def calculer_age(naissance):
    """Calcule l'âge du joueur."""
    if not naissance:
        return 0

    aujourd_hui = date.today()

    age = aujourd_hui.year - naissance.year

    if (
        (aujourd_hui.month, aujourd_hui.day)
        < (naissance.month, naissance.day)
    ):
        age -= 1

    return age


def creer_joueur():
    """Crée le joueur à partir du formulaire."""

    prenom = st.session_state.get("prenom_form", "").strip()
    nom = st.session_state.get("nom_form", "").strip()
    naissance = st.session_state.get("naissance_form")
    nationalite = st.session_state.get("nationalite_form")
    poste = st.session_state.get("poste_form")
    pied = st.session_state.get("pied_form")

    if not prenom or not nom:
        st.error("Entre ton prénom et ton nom.")
        return

    if not naissance:
        st.error("Choisis ta date de naissance.")
        return

    # Recherche d'un club adapté au niveau initial
    niveau_initial = random.randint(45, 62)

    clubs_possibles = [
        club for club in CLUBS
        if club[2] <= niveau_initial + 10
    ]

    if not clubs_possibles:
        clubs_possibles = CLUBS[:4]

    club = random.choice(clubs_possibles)

    salaire = random.randint(150, 900)

    # Création des statistiques
    if poste == "Gardien":
        technique = random.randint(48, 62)
        physique = random.randint(45, 60)
        mental = random.randint(45, 62)

    elif poste == "Défenseur":
        technique = random.randint(45, 60)
        physique = random.randint(50, 65)
        mental = random.randint(48, 63)

    elif poste == "Milieu":
        technique = random.randint(50, 65)
        physique = random.randint(45, 62)
        mental = random.randint(48, 65)

    else:
        technique = random.randint(50, 65)
        physique = random.randint(48, 63)
        mental = random.randint(45, 62)

    potentiel = random.randint(
        max(niveau_initial + 10, 60),
        min(niveau_initial + 30, 90)
    )

    st.session_state.jeu = {
        "cree": True,
        "prenom": prenom,
        "nom": nom,
        "naissance": naissance,
        "nationalite": nationalite,
        "poste": poste,
        "pied": pied,

        "club": club[0],
        "pays_club": club[1],
        "niveau_club": club[2],

        "salaire": salaire,
        "argent": 0,

        "saison": 2026,
        "semaine": 1,

        "technique": technique,
        "physique": physique,
        "mental": mental,
        "potentiel": potentiel,

        "forme": 70,
        "fatigue": 20,
        "moral": 70,

        "reputation": 10,
        "fans": 0,

        "niveau": 1,
        "experience": 0,

        "matchs": 0,
        "buts": 0,
        "passes": 0,
        "victoires": 0,
        "defaites": 0,
        "nuls": 0,

        "entrainements": 0,

        "journal": []
    }

    ajouter_journal(
        f"Début de carrière professionnelle à {club[0]}. "
        f"Contrat : {salaire} € / semaine."
    )

    st.session_state.page = "dashboard"


# ------------------------------------------------------------
# INITIALISATION
# ------------------------------------------------------------

if "jeu" not in st.session_state:
    initialiser_jeu()

if "page" not in st.session_state:
    st.session_state.page = "creation"


# ------------------------------------------------------------
# TITRE
# ------------------------------------------------------------

st.title("⚽ Football Life Simulator")

st.caption(
    "Construis ta carrière de footballeur, "
    "progresse, joue des matchs et deviens une légende."
)


# ------------------------------------------------------------
# CRÉATION DU JOUEUR
# ------------------------------------------------------------

if not st.session_state.jeu["cree"]:

    st.header("👤 Crée ton footballeur")

    col1, col2 = st.columns(2)

    with col1:
        st.text_input(
            "Prénom",
            key="prenom_form",
            placeholder="Exemple : Momo"
        )

    with col2:
        st.text_input(
            "Nom",
            key="nom_form",
            placeholder="Exemple : Roronoa"
        )

    col3, col4 = st.columns(2)

    with col3:
        st.date_input(
            "Date de naissance",
            value=date(2009, 8, 10),
            min_value=date(1985, 1, 1),
            max_value=date(2012, 12, 31),
            key="naissance_form"
        )

    with col4:
        st.selectbox(
            "Nationalité",
            NATIONALITES,
            key="nationalite_form"
        )

    col5, col6 = st.columns(2)

    with col5:
        st.selectbox(
            "Poste",
            POSTES,
            key="poste_form"
        )

    with col6:
        st.selectbox(
            "Pied préféré",
            PIEDS,
            key="pied_form"
        )

    st.divider()

    if st.button(
        "⚽ COMMENCER MA CARRIÈRE",
        type="primary",
        use_container_width=True
    ):
        creer_joueur()

else:

    # Le reste du jeu sera ajouté dans les prochains blocs.
    jeu = st.session_state.jeu

    st.success(
        f"Bienvenue {jeu['prenom']} {jeu['nom']} ! "
        f"Tu commences ta carrière à {jeu['club']}."
    )

    st.write("La création du joueur fonctionne.")
  # ============================================================
# BLOC 2/4 — TABLEAU DE BORD + ENTRAÎNEMENT
# ============================================================

def niveau_joueur():
    jeu = st.session_state.jeu

    moyenne = (
        jeu["technique"]
        + jeu["physique"]
        + jeu["mental"]
    ) / 3

    return max(1, int((moyenne - 40) / 5))


def jouer_entrainement(type_entrainement):
    jeu = st.session_state.jeu

    if jeu["fatigue"] >= 90:
        st.warning(
            "😴 Tu es trop fatigué. "
            "Prends du repos avant de t'entraîner."
        )
        return

    progression = random.randint(1, 3)

    if type_entrainement == "Technique":
        jeu["technique"] = min(
            jeu["potentiel"],
            jeu["technique"] + progression
        )
        jeu["fatigue"] += random.randint(6, 12)

        ajouter_journal(
            f"Entraînement technique : "
            f"+{progression} en technique."
        )

    elif type_entrainement == "Physique":
        jeu["physique"] = min(
            jeu["potentiel"],
            jeu["physique"] + progression
        )
        jeu["fatigue"] += random.randint(8, 15)

        ajouter_journal(
            f"Entraînement physique : "
            f"+{progression} en physique."
        )

    elif type_entrainement == "Mental":
        jeu["mental"] = min(
            jeu["potentiel"],
            jeu["mental"] + progression
        )
        jeu["fatigue"] += random.randint(4, 10)

        ajouter_journal(
            f"Travail mental : "
            f"+{progression} en mental."
        )

    elif type_entrainement == "Repos":
        jeu["fatigue"] = max(
            0,
            jeu["fatigue"] - random.randint(15, 25)
        )

        jeu["forme"] = min(
            100,
            jeu["forme"] + random.randint(5, 10)
        )

        jeu["moral"] = min(
            100,
            jeu["moral"] + random.randint(3, 8)
        )

        ajouter_journal(
            "Repos : récupération physique et mentale."
        )

    jeu["entrainements"] += 1
    jeu["experience"] += random.randint(2, 6)

    # Progression de niveau
    ancien_niveau = jeu["niveau"]
    jeu["niveau"] = niveau_joueur()

    if jeu["niveau"] > ancien_niveau:
        jeu["reputation"] += 5
        jeu["fans"] += random.randint(20, 100)

        ajouter_journal(
            f"🎉 Nouveau niveau atteint : "
            f"niveau {jeu['niveau']}."
        )


def afficher_barre(label, valeur):
    st.write(f"**{label} : {valeur}/100**")
    st.progress(max(0, min(100, valeur)) / 100)


# ------------------------------------------------------------
# NAVIGATION
# ------------------------------------------------------------

jeu = st.session_state.jeu

if jeu["cree"]:

    st.sidebar.title("⚽ MENU")

    if st.sidebar.button(
        "🏠 Tableau de bord",
        use_container_width=True
    ):
        st.session_state.page = "dashboard"

    if st.sidebar.button(
        "🏋️ Entraînement",
        use_container_width=True
    ):
        st.session_state.page = "entrainement"

    if st.sidebar.button(
        "⚽ Match",
        use_container_width=True
    ):
        st.session_state.page = "match"

    if st.sidebar.button(
        "📊 Statistiques",
        use_container_width=True
    ):
        st.session_state.page = "stats"

    if st.sidebar.button(
        "📖 Journal",
        use_container_width=True
    ):
        st.session_state.page = "journal"

    st.sidebar.divider()

    st.sidebar.write(
        f"**{jeu['prenom']} {jeu['nom']}**"
    )

    st.sidebar.write(
        f"🏟️ {jeu['club']}"
    )

    st.sidebar.write(
        f"⭐ Niveau {jeu['niveau']}"
    )


# ------------------------------------------------------------
# PAGE TABLEAU DE BORD
# ------------------------------------------------------------

if jeu["cree"] and st.session_state.page == "dashboard":

    st.header("🏠 Tableau de bord")

    st.subheader(
        f"⚽ {jeu['prenom']} {jeu['nom']}"
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "🏟️ Club",
            jeu["club"]
        )

    with col2:
        st.metric(
            "⭐ Niveau",
            jeu["niveau"]
        )

    with col3:
        st.metric(
            "💰 Argent",
            f"{jeu['argent']} €"
        )

    st.divider()

    col4, col5, col6 = st.columns(3)

    with col4:
        st.metric(
            "📅 Saison",
            jeu["saison"]
        )

    with col5:
        st.metric(
            "🗓️ Semaine",
            jeu["semaine"]
        )

    with col6:
        st.metric(
            "💵 Salaire",
            f"{jeu['salaire']} €/sem."
        )

    st.divider()

    st.subheader("📈 État du joueur")

    afficher_barre(
        "🔥 Forme",
        jeu["forme"]
    )

    afficher_barre(
        "😴 Fatigue",
        jeu["fatigue"]
    )

    afficher_barre(
        "🧠 Moral",
        jeu["moral"]
    )

    afficher_barre(
        "⭐ Réputation",
        jeu["reputation"]
    )

    st.divider()

    st.subheader("🎯 Statistiques")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Technique",
            jeu["technique"]
        )

    with c2:
        st.metric(
            "Physique",
            jeu["physique"]
        )

    with c3:
        st.metric(
            "Mental",
            jeu["mental"]
        )

    st.divider()

    st.subheader("🏆 Carrière")

    c4, c5, c6, c7 = st.columns(4)

    with c4:
        st.metric(
            "Matchs",
            jeu["matchs"]
        )

    with c5:
        st.metric(
            "Buts",
            jeu["buts"]
        )

    with c6:
        st.metric(
            "Passes",
            jeu["passes"]
        )

    with c7:
        st.metric(
            "Fans",
            jeu["fans"]
        )


# ------------------------------------------------------------
# PAGE ENTRAÎNEMENT
# ------------------------------------------------------------

elif jeu["cree"] and st.session_state.page == "entrainement":

    st.header("🏋️ Centre d'entraînement")

    st.write(
        "Améliore tes qualités pour devenir "
        "un meilleur footballeur."
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "⚽ Technique",
            use_container_width=True
        ):
            jouer_entrainement("Technique")
            st.rerun()

        if st.button(
            "💪 Physique",
            use_container_width=True
        ):
            jouer_entrainement("Physique")
            st.rerun()

    with col2:

        if st.button(
            "🧠 Mental",
            use_container_width=True
        ):
            jouer_entrainement("Mental")
            st.rerun()

        if st.button(
            "😴 Repos",
            use_container_width=True
        ):
            jouer_entrainement("Repos")
            st.rerun()

    st.divider()

    st.subheader("📊 État actuel")

    afficher_barre(
        "Technique",
        jeu["technique"]
    )

    afficher_barre(
        "Physique",
        jeu["physique"]
    )

    afficher_barre(
        "Mental",
        jeu["mental"]
    )

    afficher_barre(
        "Fatigue",
        jeu["fatigue"]
    )

    st.info(
        f"Potentiel maximum estimé : "
        f"{jeu['potentiel']}/100"
        )
  # ============================================================
# BLOC 3/4 — MATCHS + PROGRESSION
# ============================================================

def jouer_match():
    jeu = st.session_state.jeu

    if jeu["fatigue"] >= 95:
        st.error("😴 Tu es trop fatigué pour jouer ce match.")
        return

    # Niveau général du joueur
    niveau = (
        jeu["technique"]
        + jeu["physique"]
        + jeu["mental"]
    ) / 3

    performance = niveau + jeu["forme"] / 4
    performance += random.randint(-15, 15)

    # Niveau de l'adversaire
    adversaire = random.choice([
        "Racing Club",
        "United FC",
        "Sporting Club",
        "Étoile FC",
        "Olympique FC",
        "Real Sporting",
        "AS Monaco",
        "FC Nantes",
    ])

    force_adversaire = random.randint(45, 85)

    force_equipe = jeu["niveau_club"] + random.randint(-8, 8)

    buts_equipe = max(
        0,
        random.randint(0, 2)
        + int((force_equipe - force_adversaire) / 25)
    )

    buts_adversaire = max(
        0,
        random.randint(0, 2)
        + int((force_adversaire - force_equipe) / 25)
    )

    # Participation du joueur
    implication = performance / 100

    buts_joueur = 0
    passes_joueur = 0

    if jeu["poste"] == "Attaquant":
        if random.random() < max(0.15, implication):
            buts_joueur = random.choice([0, 0, 1, 1, 1, 2])

    elif jeu["poste"] == "Milieu":
        if random.random() < max(0.10, implication * 0.8):
            passes_joueur = random.choice([0, 0, 1, 1, 2])

        if random.random() < implication * 0.45:
            buts_joueur = 1

    elif jeu["poste"] == "Défenseur":
        if random.random() < implication * 0.25:
            passes_joueur = 1

    else:
        # Gardien
        if random.random() < implication * 0.08:
            passes_joueur = 1

    # On ne peut pas marquer plus de buts que son équipe
    buts_joueur = min(
        buts_joueur,
        buts_equipe
    )

    # Résultat
    if buts_equipe > buts_adversaire:
        resultat = "victoire"
        jeu["victoires"] += 1
        jeu["reputation"] += random.randint(1, 4)
        jeu["fans"] += random.randint(10, 80)

    elif buts_equipe < buts_adversaire:
        resultat = "défaite"
        jeu["defaites"] += 1
        jeu["forme"] = max(
            0,
            jeu["forme"] - random.randint(2, 7)
        )

    else:
        resultat = "match nul"
        jeu["nuls"] += 1
        jeu["reputation"] += 1
        jeu["fans"] += random.randint(3, 30)

    # Mise à jour des statistiques
    jeu["matchs"] += 1
    jeu["buts"] += buts_joueur
    jeu["passes"] += passes_joueur

    jeu["fatigue"] = min(
        100,
        jeu["fatigue"] + random.randint(12, 25)
    )

    jeu["forme"] = max(
        0,
        jeu["forme"] - random.randint(1, 6)
    )

    jeu["moral"] = max(
        0,
        min(
            100,
            jeu["moral"]
            + (
                5 if resultat == "victoire"
                else -5 if resultat == "défaite"
                else 1
            )
        )
    )

    # Expérience
    experience_gagnee = random.randint(8, 20)

    if buts_joueur:
        experience_gagnee += buts_joueur * 10

    if passes_joueur:
        experience_gagnee += passes_joueur * 7

    jeu["experience"] += experience_gagnee

    # Niveau
    nouveau_niveau = max(
        1,
        1 + jeu["experience"] // 100
    )

    niveau_monte = nouveau_niveau > jeu["niveau"]

    jeu["niveau"] = nouveau_niveau

    if niveau_monte:
        jeu["reputation"] += 10
        jeu["fans"] += random.randint(50, 250)

    # Salaire gagné
    jeu["argent"] += jeu["salaire"]

    # Journal
    detail = (
        f"Match contre {adversaire} : "
        f"{jeu['club']} {buts_equipe} - "
        f"{buts_adversaire} {adversaire}. "
    )

    if buts_joueur:
        detail += f"⚽ {buts_joueur} but(s). "

    if passes_joueur:
        detail += f"🎯 {passes_joueur} passe(s) décisive(s). "

    detail += (
        f"Résultat : {resultat}. "
        f"+{experience_gagnee} XP."
    )

    ajouter_journal(detail)

    return {
        "adversaire": adversaire,
        "buts_equipe": buts_equipe,
        "buts_adversaire": buts_adversaire,
        "buts_joueur": buts_joueur,
        "passes_joueur": passes_joueur,
        "resultat": resultat,
        "experience": experience_gagnee,
        "niveau_monte": niveau_monte
    }


# ------------------------------------------------------------
# PAGE MATCH
# ------------------------------------------------------------

if jeu["cree"] and st.session_state.page == "match":

    st.header("⚽ JOUR DE MATCH")

    st.write(
        f"🏟️ **{jeu['club']}**"
    )

    st.write(
        f"👤 {jeu['prenom']} {jeu['nom']} — "
        f"{jeu['poste']}"
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "🔥 Forme",
            f"{jeu['forme']}/100"
        )

    with col2:
        st.metric(
            "😴 Fatigue",
            f"{jeu['fatigue']}/100"
        )

    with col3:
        st.metric(
            "⭐ Niveau",
            jeu["niveau"]
        )

    st.divider()

    if st.button(
        "⚽ JOUER LE MATCH",
        type="primary",
        use_container_width=True
    ):

        resultat = jouer_match()

        if resultat:

            st.session_state.dernier_match = resultat

            st.rerun()

    if "dernier_match" in st.session_state:

        match = st.session_state.dernier_match

        st.divider()

        st.subheader("📋 Résultat")

        if match["resultat"] == "victoire":
            st.success("🏆 VICTOIRE !")

        elif match["resultat"] == "défaite":
            st.error("❌ DÉFAITE")

        else:
            st.info("🤝 MATCH NUL")

        st.markdown(
            f"""
### {jeu['club']} **{match['buts_equipe']}**
### {match['adversaire']} **{match['buts_adversaire']}**
"""
        )

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric(
                "⚽ Tes buts",
                match["buts_joueur"]
            )

        with c2:
            st.metric(
                "🎯 Tes passes",
                match["passes_joueur"]
            )

        with c3:
            st.metric(
                "✨ XP gagnée",
                match["experience"]
            )

        if match["niveau_monte"]:
            st.balloons()

            st.success(
                f"🎉 FÉLICITATIONS ! "
                f"Tu es maintenant niveau {jeu['niveau']}."
            )


# ------------------------------------------------------------
# PAGE STATISTIQUES
# ------------------------------------------------------------

elif jeu["cree"] and st.session_state.page == "stats":

    st.header("📊 Statistiques du joueur")

    st.subheader(
        f"⭐ {jeu['prenom']} {jeu['nom']}"
    )

    st.write(
        f"**Poste :** {jeu['poste']}  \n"
        f"**Pied :** {jeu['pied']}  \n"
        f"**Nationalité :** {jeu['nationalite']}"
    )

    st.divider()

    st.subheader("🎯 Attributs")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "⚽ Technique",
            jeu["technique"]
        )

    with c2:
        st.metric(
            "💪 Physique",
            jeu["physique"]
        )

    with c3:
        st.metric(
            "🧠 Mental",
            jeu["mental"]
        )

    st.divider()

    st.subheader("📈 Progression")

    c4, c5, c6 = st.columns(3)

    with c4:
        st.metric(
            "⭐ Niveau",
            jeu["niveau"]
        )

    with c5:
        st.metric(
            "✨ Expérience",
            jeu["experience"]
        )

    with c6:
        st.metric(
            "🌟 Potentiel",
            jeu["potentiel"]
        )

    st.divider()

    st.subheader("🏆 Statistiques de carrière")

    c7, c8, c9, c10 = st.columns(4)

    with c7:
        st.metric(
            "Matchs",
            jeu["matchs"]
        )

    with c8:
        st.metric(
            "Buts",
            jeu["buts"]
        )

    with c9:
        st.metric(
            "Passes",
            jeu["passes"]
        )

    with c10:
        st.metric(
            "Victoires",
            jeu["victoires"]
        )

    st.divider()

    st.subheader("💰 Vie professionnelle")

    c11, c12, c13 = st.columns(3)

    with c11:
        st.metric(
            "💵 Salaire",
            f"{jeu['salaire']} €/semaine"
        )

    with c12:
        st.metric(
            "💰 Argent",
            f"{jeu['argent']} €"
        )

    with c13:
        st.metric(
            "👥 Fans",
            jeu["fans"]
          # ============================================================
# BLOC 4/4 — JOURNAL + SEMAINE + FIN DE SAISON + RECOMMENCER
# ============================================================

def passer_semaine():
    jeu = st.session_state.jeu

    # Le salaire est versé chaque semaine
    jeu["argent"] += jeu["salaire"]

    # Récupération naturelle
    jeu["fatigue"] = max(
        0,
        jeu["fatigue"] - random.randint(4, 9)
    )

    jeu["forme"] = min(
        100,
        jeu["forme"] + random.randint(1, 5)
    )

    # Petit événement aléatoire
    evenement = random.randint(1, 8)

    if evenement == 1:
        jeu["moral"] = min(100, jeu["moral"] + 8)
        jeu["fans"] += 25
        ajouter_journal(
            "📱 Une publication sur les réseaux sociaux "
            "fait gagner 25 fans."
        )

    elif evenement == 2:
        jeu["moral"] = min(100, jeu["moral"] + 5)
        ajouter_journal(
            "😊 Ton entraîneur te félicite pour tes efforts."
        )

    elif evenement == 3:
        jeu["moral"] = max(0, jeu["moral"] - 6)
        ajouter_journal(
            "😕 Une semaine difficile affecte ton moral."
        )

    elif evenement == 4:
        prime = random.randint(50, 250)
        jeu["argent"] += prime
        ajouter_journal(
            f"💰 Tu reçois une prime de {prime} €."
        )

    elif evenement == 5:
        jeu["reputation"] += 2
        jeu["fans"] += random.randint(10, 40)
        ajouter_journal(
            "📰 Les médias commencent à parler de toi."
        )

    else:
        ajouter_journal(
            "📅 Une semaine normale de travail."
        )

    jeu["semaine"] += 1

    # Fin de saison après 38 semaines
    if jeu["semaine"] > 38:
        terminer_saison()
        return

    st.session_state.dernier_match = None


def terminer_saison():
    jeu = st.session_state.jeu

    # Récompenses de fin de saison
    bonus = 0

    if jeu["victoires"] >= 10:
        bonus += 500
        jeu["reputation"] += 5

    if jeu["buts"] >= 10:
        bonus += 750
        jeu["fans"] += 250

    if jeu["passes"] >= 10:
        bonus += 500
        jeu["fans"] += 150

    jeu["argent"] += bonus

    ajouter_journal(
        f"🏁 Fin de la saison {jeu['saison']}. "
        f"Bonus de saison : {bonus} €."
    )

    jeu["saison"] += 1
    jeu["semaine"] = 1

    # Nouvelle saison
    jeu["matchs"] = 0
    jeu["buts"] = 0
    jeu["passes"] = 0
    jeu["victoires"] = 0
    jeu["defaites"] = 0
    jeu["nuls"] = 0

    jeu["fatigue"] = 25
    jeu["forme"] = 75

    # Augmentation progressive du salaire
    jeu["salaire"] = int(
        jeu["salaire"] * 1.05
    )

    st.session_state.saison_terminee = True


# ------------------------------------------------------------
# PAGE JOURNAL
# ------------------------------------------------------------

if jeu["cree"] and st.session_state.page == "journal":

    st.header("📖 Journal de carrière")

    if not jeu["journal"]:
        st.info(
            "Ton journal est encore vide."
        )

    else:

        for evenement in jeu["journal"]:

            st.write(
                f"📌 {evenement}"
            )

            st.divider()


# ------------------------------------------------------------
# PAGE SEMAINE
# ------------------------------------------------------------

elif jeu["cree"] and st.session_state.page == "semaine":

    st.header("📅 Nouvelle semaine")

    st.write(
        f"**Saison {jeu['saison']} — "
        f"Semaine {jeu['semaine']}**"
    )

    st.divider()

    st.write(
        "Que veux-tu faire cette semaine ?"
    )

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "🏋️ Entraînement technique",
            use_container_width=True
        ):
            jouer_entrainement("Technique")
            passer_semaine()
            st.rerun()

        if st.button(
            "💪 Entraînement physique",
            use_container_width=True
        ):
            jouer_entrainement("Physique")
            passer_semaine()
            st.rerun()

    with col2:

        if st.button(
            "🧠 Entraînement mental",
            use_container_width=True
        ):
            jouer_entrainement("Mental")
            passer_semaine()
            st.rerun()

        if st.button(
            "😴 Repos",
            use_container_width=True
        ):
            jouer_entrainement("Repos")
            passer_semaine()
            st.rerun()


# ------------------------------------------------------------
# BOUTON NOUVELLE SEMAINE SUR LE TABLEAU DE BORD
# ------------------------------------------------------------

if jeu["cree"] and st.session_state.page == "dashboard":

    st.divider()

    st.subheader("📅 Gestion de ta carrière")

    if st.button(
        "➡️ PASSER À LA SEMAINE SUIVANTE",
        type="primary",
        use_container_width=True
    ):
        st.session_state.page = "semaine"
        st.rerun()


# ------------------------------------------------------------
# FIN DE SAISON
# ------------------------------------------------------------

if st.session_state.get("saison_terminee", False):

    st.divider()

    st.balloons()

    st.success(
        f"🏆 La saison {jeu['saison'] - 1} est terminée !"
    )

    st.write(
        f"Tu entres maintenant dans la saison "
        f"{jeu['saison']}."
    )

    st.metric(
        "💰 Argent disponible",
        f"{jeu['argent']} €"
    )

    if st.button(
        "▶️ COMMENCER LA NOUVELLE SAISON",
        type="primary",
        use_container_width=True
    ):
        st.session_state.saison_terminee = False
        st.session_state.page = "dashboard"
        st.rerun()


# ------------------------------------------------------------
# RECOMMENCER UNE CARRIÈRE
# ------------------------------------------------------------

if jeu["cree"]:

    st.sidebar.divider()

    if st.sidebar.button(
        "🔄 Nouvelle carrière",
        use_container_width=True
    ):
        initialiser_jeu()
        st.session_state.page = "creation"

        if "dernier_match" in st.session_state:
            del st.session_state["dernier_match"]

        if "saison_terminee" in st.session_state:
            del st.session_state["saison_terminee"]

        st.rerun()


# ------------------------------------------------------------
# PIED DE PAGE
# ------------------------------------------------------------

st.divider()

st.caption(
    "⚽ Football Life Simulator — V1"
)

      
)
  
