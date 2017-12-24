import csv, json, zipfile

UNCOMPRESSED_FILE_NAME = "Game-Analytics-EEE.json.log"
FILE_NAME = "Files/Game-Analytics-EEE.json.log.zip"
OUTPUT_FILE_NAME = "Files/data.csv"

def main():
    print("Start parssin from [" + FILE_NAME + "] json log file to [" + OUTPUT_FILE_NAME + "].")

    total_events = 0

    with zipfile.ZipFile(FILE_NAME, 'r') as zip:
        with zip.open(UNCOMPRESSED_FILE_NAME) as file:
            with open(OUTPUT_FILE_NAME, 'w', newline='') as csvfile:
                csvwriter = csv.writer(csvfile, delimiter=',')

                csvwriter.writerow(['date', 'timestamp', 'version', 'type', 'uid', 'currency', 'amount', 'iap'])

                for line in file:
                    total_events += 1
                    json_line = json.loads(line)

                    type = json_line["type"]

                    csvline = [str(json_line["date"]), str(json_line["timestamp"]), str(json_line["version"]), str(type), str(json_line["uid"])]

                    if type == "IAP_TRANSACTION":
                        csvline.append(str(json_line["currency"]))
                        csvline.append(str(json_line["amount"]))
                        csvline.append(str(json_line["iap"]))
                        #csvwriter.writerow([str(), str(), str(), str(), str(), str(), str(), str()])
                    elif type == "SESSION_START":
                        csvline.append('')
                        csvline.append('')
                        csvline.append('')

                        '''csvwriter.writerow(
                            [str(json_line["date"]), str(json_line["timestamp"]), str(json_line["version"]), str(type),
                             str(json_line["uid"])])'''

                    else:
                        print("Unknown event type: " + str(type))

                    csvwriter.writerow(csvline)

    print("Total events: " + str(total_events))


if __name__ == "__main__":
    main()