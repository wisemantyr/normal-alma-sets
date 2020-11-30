Sub CopyNewItems()
Dim lastResultsRow As Long
Dim lastReportRow As Long
Dim a As Integer
Dim b As Integer
Dim c As Integer
Dim d As Integer
Dim ws1 As Worksheet: Set ws1 = ThisWorkbook.Sheets("Sheet1")
Dim ws2 As Worksheet: Set ws2 = ThisWorkbook.Sheets("Sheet2")

lastResultsRow = ws2.Cells(ws2.Rows.Count, "A").End(xlUp).Row
lastReportRow = ws1.Cells(ws1.Rows.Count, "A").End(xlUp).Row

MsgBox ("ws1 last row: " & lastReportRow)

ws2.Columns(1).EntireColumn.Delete

For a = 2 To lastResultsRow
    resultsbar = ws2.Cells(a, 1).Value
    For b = 15 To lastReportRow
        reportbar = ws1.Cells(b, 1).Value
        If resultsbar = reportbar Then
            For c = 1 To 12
                ws2.Cells(a, c).Clear
            Next c
        End If
    Next b
Next a

For d = 2 To lastResultsRow
    If Not IsEmpty(ws2.Cells(d, 1).Value) Then
        ws2.Rows(d).Copy ws1.Rows(lastReportRow + 1)
        lastReportRow = lastReportRow + 1
    End If
Next d
        
    
End Sub
