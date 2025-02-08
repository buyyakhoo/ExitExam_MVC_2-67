import './App.css'
import React, { useState, useEffect } from 'react';
import DriverPassTypeOne from './component/DriverPassTypeOne';
import DriverPassTypeTwo from './component/DriverPassTypeTwo';
import DriverPassTypeThree from './component/DriverPassTypeThree';
import ReportDriverTypeNumber from './component/ReportDriverTypeNumber';
import ReportStatusDriver from './component/ReportStatusDriver';

interface DriverLicense {
  "DriverLicenseID": number,
  "DriverTypeID": number,
  "DriverTypeName": string,
  "BirthDay": number,
  "MonthID": number,
  "MonthName": string,
  "BirthYear": number,
  "StatusDriverID": number,
  "StatusName": string
}

function App() {

  const [handleDriverLicenseID, setHandleDriverLicenseID] = useState<string>();

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setHandleDriverLicenseID(e.target.value)
  }

  const [driverLicense, setDriverLicense] = useState<DriverLicense>()

  const handleSubmit = async () => {
    if (!handleDriverLicenseID) {
      alert("DriverLicenseID cannot be empty")
      return
    }

    if (handleDriverLicenseID.startsWith("0")) {
      alert("DriverLicenseID cannot start with 0")
      return
    }

    if (handleDriverLicenseID.length !== 9) {
      alert("DriverLicenseID must be 9 characters long")
      return
    }

    try {
      const response = await fetch("http://127.0.0.1:5000/receive_driverLicenseID", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ 
          driverLicenseID: handleDriverLicenseID, 
          driverTypeID: 1
        }),
      });

      if (!response.ok) {
        const errorData = await response.json()
        alert(`Error: ${errorData.error || "Something went wrong."}`)
        return
      }

      const data = await response.json();

      setDriverLicense({
        "DriverLicenseID": data.DriverLicenseID,
        "DriverTypeID": data.DriverTypeID,
        "DriverTypeName": data.DriverTypeName,
        "BirthDay": data.BirthDay,
        "MonthID": data.MonthID,
        "MonthName": data.MonthName,
        "BirthYear": data.BirthYear,
        "StatusDriverID": data.StatusDriverID,
        "StatusName": data.StatusName 
    })

    } catch (error) {
      console.error("Error during submission: ", error)
      alert("An error occurred while communicating with the server.");
    }
  }

  return (
    <div className="w-screen h-screen bg-blue-900 flex flex-col justify-center items-center">
      <h1 className="text-white text-6xl rounded-lg tiny5-regular"> Driver License </h1>
      <div className="flex items-center space-x-2">
        <input
            type="text"
            placeholder="input driverLicenseID"
            className="px-4 py-2 border text-white bg-blue-950 border-blue-900 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-900"
            onChange={handleInputChange}
        />
        <button
            className="px-4 py-2 text-white bg-blue-950 rounded-md hover:bg-blue-900 focus:outline-none focus:ring-2 focus:ring-blue-800"       
            onClick={handleSubmit}
        >
          input
        </button>
      </div>

      { 
        driverLicense ? (
          <div className="text-white flex-col justify-center items-center mt-3">
            {
              driverLicense.StatusDriverID === 2 || driverLicense.StatusDriverID === 3 ? (
                <p className="text-xl">ขออภัย สถานะของคุณคือ {driverLicense.StatusName}</p>
              ) : (
                driverLicense.DriverTypeID === 1 ? (
                  <DriverPassTypeOne />
                ) :
                driverLicense.DriverTypeID === 2 ? (
                  <DriverPassTypeTwo DriverLicenseID={handleDriverLicenseID || ''} />
                ) : 
                driverLicense.DriverTypeID === 3 ? (
                  <DriverPassTypeThree />
                ) : null
              )
            }

          </div>
        ) : null
      }


      <ReportDriverTypeNumber />
      <ReportStatusDriver />
    </div>
  )
}

export default App
