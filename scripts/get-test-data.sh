#!/bin/bash
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd $SCRIPT_DIR
cd ..
mkdir -p testdata
cd testdata
SHAOUT=($(cat *.adc *.hdr *.roi | sha256sum -b))
SHAOUT=${SHAOUT[0]}
if [ "$SHAOUT" = "692ece92694019cf15a85a0012c1191aa0f88f86b919fbb0902317b8d350469e" ]; then
    echo "Test data OK, skipping download"
else
    echo "Test data hash ($SHAOUT) did not match expected output, redownloading data"
    rm *.adc *.hdr *.roi
    wget https://ifcb-data.whoi.edu/IFCB14_dock_WHOI/D20140117T003426_IFCB014.adc
    wget https://ifcb-data.whoi.edu/IFCB14_dock_WHOI/D20140117T003426_IFCB014.hdr
    wget https://ifcb-data.whoi.edu/IFCB14_dock_WHOI/D20140117T003426_IFCB014.roi
    wget https://ifcb-data.whoi.edu/NAAMES/D20180402T125812_IFCB107.adc
    wget https://ifcb-data.whoi.edu/NAAMES/D20180402T125812_IFCB107.hdr
    wget https://ifcb-data.whoi.edu/NAAMES/D20180402T125812_IFCB107.roi
    wget https://ifcb-data.whoi.edu/WHOI_dock/D20250304T154126_IFCB127.adc
    wget https://ifcb-data.whoi.edu/WHOI_dock/D20250304T154126_IFCB127.hdr
    wget https://ifcb-data.whoi.edu/WHOI_dock/D20250304T154126_IFCB127.roi
fi
