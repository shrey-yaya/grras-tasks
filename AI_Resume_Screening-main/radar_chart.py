import matplotlib.pyplot as plt
import numpy as np

def plot_radar(user_scores, required_scores, labels, title="Skill Gap Analysis"):
    num_vars = len(labels)

    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

    user_scores += user_scores[:1]
    required_scores += required_scores[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

    ax.plot(angles, user_scores, linewidth=2, label="You")
    ax.fill(angles, user_scores, alpha=0.25)

    ax.plot(angles, required_scores, linewidth=2, label="Job Requirement")
    ax.fill(angles, required_scores, alpha=0.15)

    ax.set_thetagrids(np.degrees(angles[:-1]), labels)

    ax.set_title(title)
    ax.legend(loc="upper right")

    return fig