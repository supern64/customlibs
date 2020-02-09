package com.sn.MultiplayerTools;

import java.util.Map;

import static java.lang.Math.pow;
import static java.lang.Math.round;

public class LibRanking {
    public static class RankingBoard {
        private Map<String, Integer> rankings;
        private Integer startingPoints;
        private Integer variation;
        private Integer maxScore;
        private boolean isInfinite;
        private boolean allowNegatives;

        public RankingBoard(Map<String, Integer> ranking, Integer start, Integer maxV, Integer maxS, boolean allowNegative) {
            rankings = ranking;
            startingPoints = start;
            variation = maxV;
            allowNegatives = allowNegative;
            if (maxS <= 0) {
                isInfinite = true;
                maxScore = 0;
            } else {
                isInfinite = false;
                maxScore = maxS;
            }
        }
        public void createPlayer(String playerId) {
            rankings.put(playerId, startingPoints);
        }
        public MatchResult recordMatch(String opponentId1, String opponentId2, boolean results) {
            Integer ratingOp1 = rankings.get(opponentId1);
            Integer ratingOp2 = rankings.get(opponentId2);

            double Op1Probability = (1.0 / (1.0 + pow(10, ((ratingOp2 - ratingOp1) / 400))));
            double Op2Probability = (1.0 / (1.0 + pow(10, ((ratingOp1 - ratingOp2) / 400))));

            Integer Op1Score;
            Integer Op2Score;

            if (results == true) {
                Op1Score = 1;
                Op2Score = 0;
            } else {
                Op1Score = 0;
                Op2Score = 1;
            }
            Integer Op1Gain = Math.toIntExact(round(variation * (Op1Score - Op1Probability)));
            Integer Op2Gain = Math.toIntExact(round(variation * (Op2Score - Op2Probability)));

            ratingOp1 = ratingOp1 + Op1Gain;
            ratingOp2 = ratingOp2 + Op2Gain;

            if (!allowNegatives) {
                if (ratingOp1 < 0) {
                    ratingOp1 = 0;
                }
                if (ratingOp2 < 0) {
                    ratingOp2 = 0;
                }
            }

            if (ratingOp1 > maxScore && !isInfinite) {
                ratingOp1 = maxScore;
            }
            if (ratingOp2 > maxScore && !isInfinite) {
                ratingOp2 = maxScore;
            }

            MatchResult result = new MatchResult();
            result.Op1Gain = Op1Gain;
            result.Op2Gain = Op2Gain;

            result.Op1Point = ratingOp1;
            result.Op2Point = ratingOp2;

            rankings.put(opponentId1, ratingOp1);
            rankings.put(opponentId2, ratingOp2);

            return result;
        }
        public Map<String, Integer> getRankings() {
            return rankings;
        }
    }
    public static class MatchResult {
        public Integer Op1Gain;
        public Integer Op2Gain;

        public Integer Op1Point;
        public Integer Op2Point;

        public MatchResult() {}
    }
}