# GovHack23 Solution Statement
The data acquisition process commenced with the extraction of data from the UnityWater dataset, which was subsequently processed and organized within an SQL database, facilitating enhanced data manipulation capabilities.

#### Example of Telemetry Data
<img src="https://github.com/beomusxyz/GovHack23/blob/master/images/eda_on_telemetry.png?raw=true" alt="Data Example" width="600" style="max-width: 50%;"/>

In pursuit of geographical insight, locations of UnityWater sites and service points were geospatially visualized using cartographic representations. Subsequently, the conversion of street addresses to latitude and longitude coordinates was accomplished via the QLD Government Geocode Checker, ensuring spatial precision. This culminated in the computation of distances between UnityWater sites and service points, essential for subsequent analyses. Analyses such as plotting the vehicle movement between the various sites, to display the current level of inefficiencies present in the organisation of vehicle resources.

#### Current UnityWater Centers
<img src="https://github.com/beomusxyz/GovHack23/blob/master/images/current_centers.png" alt="Original Locations" width="300" style="max-width: 50%;"/>

#### Incident Location Heatmap
<img src="https://github.com/beomusxyz/GovHack23/blob/master/images/heatmap_of_incidences.png" alt="Incident Location Heatmap" width="300" style="max-width: 50%;"/>

#### Current Vehicle Movement
<img src="https://github.com/beomusxyz/GovHack23/blob/master/images/vehicle%20movement.png" alt="Current Vehicle Movement" width="300" style="max-width: 50%;"/>

Harnessing the elbow method, optimal values of K-means clustering centroids were derived, substantiating the identification of strategic placements for future UnityWater service sites. This strategic expansion aimed to curtail response time while minimizing both vehicular hours on the road and carbon emissions. The process involved a meticulous balance between the count of potential new centers and an acceptable threshold for response time, thereby substantiating the feasibility of the proposed site distribution.

#### Full K Mean Values
<img src="https://github.com/beomusxyz/GovHack23/blob/master/images/kmeans_full.png?raw=true" alt="Full K Mean Values" width="700" style="max-width: 50%;"/>

#### Truncated K Mean Values
<img src="https://github.com/beomusxyz/GovHack23/blob/master/images/kmeans_full.png" alt="Truncated K Mean Values" width="700" style="max-width: 50%;"/>
Proposed recommendations entail five prospective sites, and their respective zones of operation. Strategically pinpointed based on data-driven insights, all aimed at ameliorating staff road hours and, by extension, mitigating carbon emissions. Furthermore, an avenue for prospective exploration is envisioned, focused on ameliorating emissions. This extension involves a rigorous examination of the viability of electrifying a subset of the UnityWater fleet characterized by lower range requirements. This inquiry necessitates the aggregation of data pertaining to idle times at service centers and locations equipped with electric vehicle (EV) infrastructure. Leveraging this information, the implementation of opportunity charging surfaces as a solution to range limitations for UnityWater vehicles emerges as a potential technique warranting further exploration.

#### Colour Coded Zones of Operations and Their Respective Sites
<img src="https://github.com/beomusxyz/GovHack23/blob/master/images/proposed_centers.png?raw=true" alt="Colour Coded Zones of Operations and Their Respective Sites" width="300" style="max-width: 50%;"/>
In summary, the convergence of data science techniques, spatial analysis, and optimization methodologies has culminated in a comprehensive proposal for enhancing UnityWater's operational efficiency, environmental sustainability, and response effectiveness. The proposition of future directions, including both expansion strategies and the exploration of EV adoption, underscores the data-driven and forward-thinking nature of this solution.
