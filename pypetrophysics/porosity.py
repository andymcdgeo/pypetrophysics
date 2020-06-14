class Porosity:

    def limit_vals(self, input_value, low_limit, high_limit):
        """
        Apply limits to an input value.

        Parameters
        ----------
        input_value : float
            Input value.
        low_limit : float
            Low limit. If value falls below this limit it will be set to this value.
        high_limit : float
            High limit. If value falls above this limit it will be set to this value.

        Returns
        -------
        float
            Returns input value unless it falls above or below the entered limits.
        """
        if input_value < low_limit:
            return low_limit
        elif input_value > high_limit:
            return high_limit
        else:
            return input_value

    def porosity_density(self, rhomatrix, rhofluid, rhobulk, limit_result=False, low_limit=0, high_limit=0.6):
        """
        Calculate porosity from a density log

        Parameters
        ----------
        rhomatrix : float
            Matrix density. 
            
            Typical values:
              Sandstone: 2.65 g/cc
              Limestone: 2.71 g/cc
              Dolomite: 2.80 - 2.85 g/cc
        rhofluid : float
            Fluid density.
        rhobulk : float
            Bulk density from log measurements
        limit_result : bool, optional
            Apply limits to the result value.
            By default False
        low_limit : int, optional
            Low limit. If value falls below this limit it will be set to this value. 
            By default 0
        high_limit : float, optional
            High limit. If value falls above this limit it will be set to this value.
            By default: 0.6

        Returns
        -------
         float
            Density porosity value in decimal units.
        """
        porosity = (rhomatrix - rhobulk)/(rhobulk - rhofluid)

        if limit_result is True:
            return self.limit_vals(porosity, low_limit, high_limit)
        else:
            return porosity
            
    def porosity_sonic(self, dtmatrix, dtfluid, dtlog, method="wylie", limit_result=False, low_limit=0, high_limit=0.6):
        """
        Caculate porosity from a sonic log using either the Wylie-Time Average equation
        or Raymer-Hunt-Gardener equation.

        Parameters
        ----------
        dtmatrix : float
            Matrix slowness.

            Typical values:
              Sandstone: 52-55 us/ft
              Limestone: 47 us/ft
              Dolomite: 43 us/ft
        dtfluid : float
            Fluid slowness.
        dtlog : [type]
            Slowness (DT) from log measurements.
        method : string
            Select a method for calculating sonic porosity:
            "wylie" - Wylie Time Average (default)
            "raymer" - Raymer Hunt Gardener
        limit_result : bool, optional
            Apply limits to the result value.
            By default False
        low_limit : int, optional
            Low limit. If value falls below this limit it will be set to this value. 
            By default 0
        high_limit : float, optional
            High limit. If value falls above this limit it will be set to this value.
            By default: 0.6

        Returns
        -------
        float
            Sonic porosity value in decimal units.

        Raises
        ------
        Exception
            Raise an exception if method value is not 1 or 2.

        References
        ----------
        Wyllie, M.R.J., Gregory, A.R., and Gardner, L.W. 1956. Elastic Wave Velocities in Heterogeneous and Porous Media. Geophysics 21 (1): 41–70.
        Raymer, L.L., Hunt, E.R., and Gardner, J.S. 1980. An Improved Sonic Transit Time-to-Porosity Transform, paper P. Trans., 1980 Annual Logging Symposium, SPWLA, 1–12.
        """
        if method == "wylie": #Wylie Time Average
            porosity = (dtlog - dtmatrix) / (dtfluid - dtmatrix)
        elif method == "raymer": #Raymer Hunt Gardener 
            alpha = (dtmatrix / (2 * dtfluid)) - 1
            porosity = -alpha-((alpha**2 + (dtmatrix / dtlog)-1)**0.5)
        else:
            raise Exception("Enter a valid method value: wylie or raymer")

        if limit_result is True:
            return self.limit_vals(porosity, low_limit, high_limit)
        else:
            return porosity
