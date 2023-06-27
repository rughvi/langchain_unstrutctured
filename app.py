from fileReader import FileReader
from fileProcessors.medicalRecordProcessor import MedicalRecordProcessor
from dotenv import load_dotenv

load_dotenv()
# NO NEED os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

def main():
    filePath = 'PatientMedicalRecord.pdf'
    # fileReader = FileReader()
    # text = fileReader.readFile(filePath)

    medicalRecordProcessor = MedicalRecordProcessor()
    medicalRecord = medicalRecordProcessor.processText(filePath)
    print(medicalRecord)
    
# Call main
main()