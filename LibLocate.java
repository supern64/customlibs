package com.sn.MultiplayerTools;

import static java.lang.Math.sin;
import static java.lang.Math.cos;
import static java.lang.Math.toRadians;
import static java.lang.Math.atan2;
import static java.lang.Math.sqrt;


public class LibLocate {
    final static double radius = 6371e3;
    public static double findDistance(double latitude1, double longitude1, double latitude2, double longitude2) {
        double lat1Radius = toRadians(latitude1);
        double lat2Radius = toRadians(latitude2);

        double latDiffRadius = toRadians(latitude2 - latitude1);
        double lonDiffRadius = toRadians(longitude2 - longitude1);

        double a = sin(latDiffRadius/2) * sin(latDiffRadius/2)  + cos(lat1Radius) * cos(lat2Radius) * sin(lonDiffRadius/2) * sin(lonDiffRadius/2);
        double c = 2 * atan2(sqrt(a), sqrt(1-a));

        double distance = radius * c;
        return distance;
    }
    public static double dmsToDecimals(double degrees, double minutes, double seconds) {
        return degrees + (minutes/60) + (seconds/3600);
    }
}
