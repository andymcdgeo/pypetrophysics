from miscfuncs import limit_vals

class ClayShale:
    
    def gr_index(self, minvalue, maxvalue, inputvalue, limit_result=False, low_limit=0, high_limit=1):
        igr = (inputvalue - minvalue)/(maxvalue - minvalue)

        if limit_result is True:
            return limit_vals(igr, low_limit, high_limit)
        else:
            return igr

    def vsh_larionov_tertiary(self, minvalue, maxvalue, inputvalue, limit_result=False, low_limit=0, high_limit=1):
        igr = self.gr_index(minvalue, maxvalue, inputvalue, limit_result, low_limit, high_limit)
        return 0.083 * ((2**(3.71 * igr)) - 1)

    def vsh_larionov_older(self, minvalue, maxvalue, inputvalue, limit_result=False, low_limit=0, high_limit=1):
        igr = self.gr_index(minvalue, maxvalue, inputvalue, limit_result, low_limit, high_limit)
        return 0.33 * ((2**(2 * igr)) - 1)

    def vsh_steiber(self, minvalue, maxvalue, inputvalue, limit_result=False, low_limit=0, high_limit=1):
        igr = self.gr_index(minvalue, maxvalue, inputvalue, limit_result, low_limit, high_limit)
        return igr / (3 - 2 * igr)

    def vsh_clavier(self, minvalue, maxvalue, inputvalue, limit_result=False, low_limit=0, high_limit=1):
        igr = self.gr_index(minvalue, maxvalue, inputvalue, limit_result, low_limit, high_limit)
        return 1.7 - ((3.38-(igr + 0.7)**2)**0.5)