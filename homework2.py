#Title: free flow speed calculator for basic highway segment
print("Free Flow Speed Calculator for a Basic Highway Segment Per NCEES 2026")

#ask user for inputs
BFFS=(75.4)
flw=float(input("Enter the lane width adjustment (mph)"))
frlc=float(input("Enter the right-side lateral clearance adjustment (mph)"))
TRD=float(input("Enter the total ramp density (ramps per mile)"))

#calculate the free flow speed
FFS=BFFS-flw-frlc-3.22*(TRD**0.84)

#display the result
print("The free flow speed is:",FFS, "mph")