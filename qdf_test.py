
import QDF



# fname = '../xx_WP1_20-11-23-full-confl_Well1_PC-3_untreated_manualni sltacovani_phase.qdf'
fname = '../2fsfsd.qdf'

reader = QDF.reader(fname)
main_info = reader.main_info



for c in reader.ranges['c']:
    for t in range(reader.ranges[c]['t'] + 1):
        for p in range(reader.ranges[c]['p'] + 1):
            for z in range(reader.ranges[c]['z'] + 1):
                img = reader.get_image(c, t, p, z)
                img_info = reader.get_image_info(c, t, p, z)
                break




# from cdflib_custom.cdfread import CDF

# fname = '../xx_WP1_20-11-23-full-confl_Well1_PC-3_untreated_manualni sltacovani.cdf'
# cdf_file = CDF(fname)


# info = cdf_file.cdf_info()

# timestamp_info = cdf_file.varinq('timestamp')


# times = cdf_file.varget('time-Hologram')


# holograms = cdf_file.varget('pos-Hologram')