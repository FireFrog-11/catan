def get_scale_factors(screen):
    scale_factor_x = screen.get_size()[0] / 1536
    scale_factor_y = screen.get_size()[1] / 864
    return (scale_factor_x, scale_factor_y)