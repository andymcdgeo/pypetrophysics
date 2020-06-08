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
            Compute matrix density. 
            
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
            Porosity value in decimal units.
        """
        porosity = (rhomatrix - rhobulk)/(rhobulk - rhofluid)

        if limit_result is True:
            return self.limit_vals(porosity, low_limit, high_limit)
        else:
            return porosity
            
