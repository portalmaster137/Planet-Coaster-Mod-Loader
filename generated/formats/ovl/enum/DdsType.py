from generated.enum import UbyteEnum


class DdsType(UbyteEnum):

	"""
	maps the OVL's dds type to name of compression format
	"""
	DXGI_FORMAT_R8G8B8A8_UNORM = 35
	# gharial_male.pclut.dds, or DXGI_FORMAT_D24_UNORM_S8_UINT, DXGI_FORMAT_R8G8B8A8_UNORM
	DXGI_FORMAT_R8G8B8A8_UNORM_SRGB = 37
	# atmospherics_stars_data.dds
	DXGI_FORMAT_D32_FLOAT_S8X24_UINT = 38
	DXGI_FORMAT_R16G16_FLOAT = 43
	DXGI_FORMAT_BC1_UNORM = 78
	DXGI_FORMAT_BC1_UNORM_SRGB = 79
	DXGI_FORMAT_BC2_UNORM = 80
	DXGI_FORMAT_BC2_UNORM_SRGB = 81
	# PZ wolf baldnessscars texture
	DXGI_FORMAT_BC3_UNORM = 82
	DXGI_FORMAT_BC3_UNORM_SRGB = 83
	DXGI_FORMAT_BC4_UNORM = 84
	DXGI_FORMAT_BC4_SNORM = 85
	DXGI_FORMAT_BC5_UNORM = 86
	DXGI_FORMAT_BC5_SNORM = 87
	# ptero aviary
	DXGI_FORMAT_BC6H_UF16 = 88
	DXGI_FORMAT_BC6H_SF16 = 89
	DXGI_FORMAT_BC7_UNORM = 90
	# PZ titan beetle
	DXGI_FORMAT_BC7_UNORM_SRGB = 91
