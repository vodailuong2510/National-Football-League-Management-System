from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Match, Ranking

@receiver(post_save, sender=Match)
def update_rankings(sender, instance, **kwargs):
    league = instance.LEAGUEID
    home_team = instance.HOMETEAM
    away_team = instance.AWAYTEAM
    home_score = instance.HOMESCORE
    away_score = instance.AWAYSCORE

    if home_score is not None and away_score is not None:
        home_ranking, created = Ranking.objects.get_or_create(LEAGUE=league, CLUB=home_team)
        away_ranking, created = Ranking.objects.get_or_create(LEAGUE=league, CLUB=away_team)

        if home_score > away_score:
            home_ranking.WON += 1
            home_ranking.POINTS += 3
            away_ranking.LOST += 1
        elif home_score < away_score:
            away_ranking.WON += 1
            away_ranking.POINTS += 3
            home_ranking.LOST += 1
        else:
            home_ranking.DRAWN += 1
            away_ranking.DRAWN += 1
            home_ranking.POINTS += 1
            away_ranking.POINTS += 1

        home_ranking.PLAYED += 1
        home_ranking.GOALS_FOR += home_score
        home_ranking.GOALS_AGAINST += away_score
        home_ranking.GOAL_DIFFERENCE = home_ranking.GOALS_FOR - home_ranking.GOALS_AGAINST

        away_ranking.PLAYED += 1
        away_ranking.GOALS_FOR += away_score
        away_ranking.GOALS_AGAINST += home_score
        away_ranking.GOAL_DIFFERENCE = away_ranking.GOALS_FOR - away_ranking.GOALS_AGAINST

        home_ranking.save()
        away_ranking.save()