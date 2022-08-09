class Invoice
    # class method
    def self.print_out
       "Printed out invoice"
    end
    # instance method
    def convert_to_pdf
       "Converted to PDF"
    end

end

p Invoice.print_out
i = Invoice.new
p i.convert_to_pdf