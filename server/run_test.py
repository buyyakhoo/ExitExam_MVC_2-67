from src.model import DriverLicenseModel

dl = DriverLicenseModel()
# print(cm.get_all_colors())
print(dl.get_all_driver_license())
print("=== SUCCESS ON GET ALL DRIVER LICENSE ===")
print(dl.get_specific_driver_license(100000083))
# print("=== SUCCESS ON GET SPECIFIC DRIVER LICENSE ===")
print(dl.get_age_of_driver_license(100000083))