#!/usr/bin/env ruby
#
require 'csv'

if __FILE__ == $0
  repr = CSV.read(ARGV.shift)
  print repr.class
  CSV.open(ARGV.shift, "wb") do |csv|
    repr.each do |row|
      csv << row
    end
  end
end
